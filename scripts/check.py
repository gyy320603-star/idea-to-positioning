"""Check the skill's documentation and optionally build its installable ZIP."""

import argparse
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tempfile
from urllib.parse import unquote, urlsplit
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
NAME = "idea-to-positioning"
DOCUMENTS = ("SKILL.md", "README.md", "CHANGELOG.md", "CONTRIBUTORS.md", "LICENSE")
ASSET_DIRS = ("references", "templates", "examples")
MODES = {"grill", "one-page", "full", "front-stage", "work", "campaign"}
CORE = {"00_DECISION_BRIEF.md", "01_DECK_OUTLINE.md", "02_GRILL_LOG.md", "03_SOURCES.md"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def release_version(root):
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    header = re.match(r"^---\n(.*?)\n---\n", skill, re.DOTALL)
    require(header, "SKILL.md is missing its YAML frontmatter")
    fields = header.group(1)
    require(re.findall(r"^name: (.+)$", fields, re.M) == [NAME], "unexpected skill name")
    versions = re.findall(r"^version: (.+)$", fields, re.M)
    require(len(versions) == 1 and re.fullmatch(r"\d+\.\d+\.\d+", versions[0]),
            "SKILL.md needs one numeric semantic version")
    version = versions[0]
    changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
    latest = re.search(r"^## (\d+\.\d+\.\d+)\b", changelog, re.M)
    require(latest and latest.group(1) == version, "CHANGELOG.md and SKILL.md versions differ")
    readme = (root / "README.md").read_text(encoding="utf-8")
    declared = re.search(r"^Version (\d+\.\d+\.\d+)\b", readme, re.M)
    require(declared and declared.group(1) == version,
            "README.md and SKILL.md versions differ")
    archives = set(re.findall(re.escape(NAME) + r"-(\d+\.\d+\.\d+)\.zip", readme))
    require(archives == {version}, "README.md must name the current release ZIP")
    return version


def payload(root):
    files = [root / name for name in DOCUMENTS]
    for directory in ASSET_DIRS:
        assets = [p for p in (root / directory).rglob("*.md")
                  if not any(part.startswith(".") or part == "__pycache__"
                             for part in p.relative_to(root).parts)]
        require(assets, f"missing Markdown content in {directory}/")
        files.extend(assets)
    for file in files:
        require(file.is_file() and file.resolve() == file,
                f"missing or symlinked release file: {file.relative_to(root)}")
    return sorted(files)


def check_links(root, files):
    # Markdown links are relative to the referring page. Backticked skill asset
    # paths use the skill root (e.g. references/foo.md in a nested reference).
    asset_path = re.compile(r"`((?:references|templates|examples)/[^`\n]*)`")
    markdown_link = re.compile(r"\]\((?:<([^>]+)>|([^\s)]+))(?:\s+\"[^\"]*\")?\)")
    for file in files:
        if file.suffix != ".md":
            continue
        for number, line in enumerate(file.read_text(encoding="utf-8").splitlines(), 1):
            location = f"{file.relative_to(root)}:{number}"
            for path in asset_path.findall(line):
                target = (root / path).resolve()
                require(target.is_relative_to(root) and target.exists(),
                        f"{location}: missing skill asset {path}")
            for angle_path, bare_path in markdown_link.findall(line):
                link = urlsplit(angle_path or bare_path)
                if link.scheme or link.netloc:
                    continue
                path = unquote(link.path)
                target = (file.parent / path).resolve() if path else file
                require(target.is_relative_to(root) and target.exists(),
                        f"{location}: broken local link {path}")
                if link.fragment and target.suffix == ".md":
                    headings = re.findall(r"^#{1,6}\s+(.+)$", target.read_text(encoding="utf-8"), re.M)
                    anchors = {re.sub(r"[^\w -]", "", h.lower()).strip().replace(" ", "-")
                               for h in headings}
                    require(unquote(link.fragment) in anchors,
                            f"{location}: missing section {path}#{link.fragment}")


def code_cell(cell, location):
    match = re.fullmatch(r"`([^`]+)`", cell)
    require(match, f"{location}: expected one backticked path, got {cell!r}")
    return match.group(1)


def check_outputs(root):
    manifest = root / "references/outputs.md"
    rows = [(i, line.strip()) for i, line in
            enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1)
            if line.lstrip().startswith("|")]
    require(len(rows) >= 3 and rows[0][1] == "| Mode | Template | Project path |",
            "references/outputs.md needs the Mode / Template / Project path table")
    require(re.fullmatch(r"\|(?:\s*:?-{3,}:?\s*\|){3}", rows[1][1]),
            "references/outputs.md has an invalid table separator")
    routes = {mode: set() for mode in MODES}
    for number, row in rows[2:]:
        location = f"references/outputs.md:{number}"
        cells = [c.strip() for c in row.strip("|").split("|")]
        require(len(cells) == 3, f"{location}: expected three columns")
        mode, source, destination = cells
        require(mode in MODES, f"{location}: unknown mode {mode}")
        if source != "—":
            template = code_cell(source, location)
            require(re.fullmatch(r"templates/[\w.-]+\.md", template)
                    and (root / template).is_file(), f"{location}: invalid template {template}")
        path = code_cell(destination, location)
        project_path = PurePosixPath(path)
        # Only project output roots are allowed. This rejects installed templates,
        # absolute paths, parent hops, OS-specific separators and shell variables.
        require(re.fullmatch(r"[\w.-]+(?:/[\w.-]+)*/?", path)
                and not any(part.startswith(".") for part in path.rstrip("/").split("/"))
                and (path == "GRILL.md" or
                     project_path.parts[0] in {"delivery", "work", "appendix", "campaign"}),
                f"{location}: unsafe project output {path}")
        require(not path.endswith("/") or (mode == "campaign" and path == "campaign/"),
                f"{location}: expected a project file, got {path}")
        require(path not in routes[mode], f"{location}: duplicate {mode} output {path}")
        routes[mode].add(path)
    require(all(routes.values()), "the output table must cover every mode")
    require(routes["grill"] == {"GRILL.md"}, "single-grill mode must output only GRILL.md")
    require(routes["one-page"] == {"delivery/00_DECISION_BRIEF.md", "delivery/03_SOURCES.md"},
            "one-page mode must output the brief and sources")
    require({"delivery/" + name for name in CORE} <= routes["full"],
            "full mode is missing a core delivery")


def package(root, files, version, directory):
    directory = directory.resolve()
    directory.mkdir(parents=True, exist_ok=True)
    filename = f"{NAME}-{version}.zip"
    expected = {f"{NAME}/{p.relative_to(root).as_posix()}": p for p in files}
    with tempfile.TemporaryDirectory(dir=directory) as stage:
        archive = Path(stage) / filename
        with ZipFile(archive, "w") as bundle:
            for name, source in expected.items():
                entry = ZipInfo(name)  # Fixed timestamp makes repeat builds comparable.
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                bundle.writestr(entry, source.read_bytes(), compress_type=ZIP_DEFLATED)
        extracted = Path(stage) / "unpacked"
        with ZipFile(archive) as bundle:
            require(bundle.namelist() == list(expected), "unexpected ZIP layout")
            require(bundle.testzip() is None, "ZIP integrity check failed")
            bundle.extractall(extracted)
        installed = Path(stage) / "skills" / "marketing" / NAME
        shutil.copytree(extracted / NAME, installed)
        for name, source in expected.items():
            path = installed / PurePosixPath(name).relative_to(NAME)
            require(path.read_bytes() == source.read_bytes(), f"install mismatch: {name}")
        require(release_version(installed) == version, "installed version mismatch")
        check_outputs(installed)
        check_links(installed, payload(installed))
        archive.replace(directory / filename)
    return directory / filename


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path, metavar="DIR",
                        help="also build and verify an installable ZIP in DIR")
    args = parser.parse_args()
    try:
        version = release_version(ROOT)
        files = payload(ROOT)
        check_links(ROOT, files)
        check_outputs(ROOT)
        if args.package is not None:
            print(f"Verified {package(ROOT, files, version, args.package)}")
        print(f"Validated {NAME} {version} ({len(files)} release files)")
    except (ValueError, OSError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
