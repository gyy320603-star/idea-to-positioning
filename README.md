# idea-to-positioning

**Turn a topic or concept into a defensible position.**

Version 1.0.1 · MIT · Author: Yuyang Gong (龚雨旸)

## What it is

A stage-gated discovery skill for early-stage brand, product, and coursework projects.

It is not a “generate 50 ideas” prompt. It is a funnel:

```
constraints → concepts → kills → evidence → positioning → deck → grill → decision
```

The goal is not more output. The goal is a smaller number of claims that survive evidence and adversarial review.

## When to use

- You have a topic but no product, scene, or audience.
- You have a concept and need to stress-test it before making a deck.
- You need a positioning and audience from public evidence.
- You want a “grill me” review that ends in a decision, not a debate.
- You want to run a multi-batch campaign on one topic and select the best survivors.

Do not use for visual identity execution, production CAD, or media buying. Those come after positioning.

## Input

You do not need to supply links, audience, or delivery format.

| Tier | You give | The skill does |
|---|---|---|
| 1 | Topic only | Public scan, 2–3 candidate frames, pick the strongest, list runners-up. |
| 2 | Topic + scene/persona | Treat it as an assumption; test it; keep, narrow, or reject. |
| 3 | Topic + links | Use the links first, supplement, record dates. |

No fabricated interviews. No invented prices. No “no one does this” absolutes.

## Request modes

| Request | You get | You do not get |
|---|---|---|
| **Full positioning**: topic only, or topic + hypothesis | Decision brief, **8-page deck outline (default)**, grill log, source table, appendix | A deck built before the claim survives |
| **One-page only**: explicit request | Decision brief + source table | A deck |
| **Single grill**: existing claim/concept | One-page `GRILL.md`: verdict, strongest challenge, evidence status, deleted sentence, decision, next evidence | An 8-page deck unless you ask |
| **Campaign / multi-batch** | Campaign folder, funnel counts, blind review at milestones, only finalists | 100 decks; a winner before blind review |

**Default rule:** full positioning gets 8 pages. A one-page brief is a separate mode and happens only when the user explicitly asks for one page.

## Workflow and deliverables

The gates take a topic from a scene and its constraints through concept screening, evidence review, positioning, and a decision to continue, narrow, pivot, or stop. Each gate lists the questions to answer and when to move forward. [Positioning workflow](references/workflow.md)

For each request mode, the output table identifies the template to read and the destination to write in the user's project. Keep the installed templates available for the next run. [Project output paths](references/outputs.md)

For students and teachers, open with a short reading guide that states the recommendation, the biggest unknown, and the next cheapest action. Present the proposal and evidence in plain language, with working notes available separately. [Front-stage guide](references/front-stage-output.md)

## Evidence thresholds

- **Screening:** two independent sources that agree can advance a concept to the next gate.
- **Key claim:** three independent sources, including at least one non-self-report source (official rule, product page, observed behaviour, or dated first-hand account).
- **Fewer than three:** label `[assumption]` or `[self-report]`; do not call it proven.
- **Conflict:** report it; do not average it or stop at a false consensus.

## Core rules

- Define **Who by behaviour**, not demographics.
- Separate the **initiator** from the **companion** in a two-person occasion.
- A feature gap is not demand.
- A mention is not a decision-changing constraint.
- Keep one promise; a slogan is not the What.
- Label evidence: `[course pXX]`, `[group-confirmed]`, `[observed]`, `[self-report]`, `[inferred]`, `[assumption]`, `[not found]`.
- Every grill must delete a sentence, change a decision, or write a kill criterion.
- Do not start logo, VI, packaging, or campaign before positioning survives.

## Install

For the v1.0.1 GitHub release, select the asset named `idea-to-positioning-1.0.1.zip`. Unzip it, then run the commands below from the directory containing the extracted `idea-to-positioning/` folder. [GitHub releases](https://github.com/gyy320603-star/idea-to-positioning/releases)

**macOS**

```bash
mkdir -p ~/.hermes/skills/marketing
cp -R idea-to-positioning ~/.hermes/skills/marketing/
hermes skills list
```

**Windows**

```powershell
$dest = Join-Path $env:LOCALAPPDATA "hermes\skills\marketing"
New-Item -ItemType Directory -Force $dest | Out-Null
Copy-Item -Recurse .\idea-to-positioning $dest
hermes skills list
```

Then load it by name:

```
skill_view(name="idea-to-positioning")
```

## Quick prompts

```text
我只有一个选题：<topic>。请按 idea-to-positioning 跑第一轮。
```

```text
帮我 grill 这个想法：<claim>。只要质询和决定，不要 8 页 deck。
```

```text
围绕这个选题跑一个 3 批 campaign：<topic>。每批 10 个概念，最后盲评选 1 个。
```

```text
我只要一页：<topic>。给我 decision brief 和来源表，不要 deck。
```

```text
把这次产出整理成学生能看的前台版：00_先读我 + 一页结论 + 八页提案 + 依据与风险。
```

## Repository guide

Start with the [skill entry point](SKILL.md) to see which procedure each request triggers. The [references](references/) explain the method and the [templates](templates/) supply the working forms.

## Check and package a release

From a source checkout, run the documentation checks with Python 3.9 or later.

```bash
python3 scripts/check.py
```

To run the checks, build the installable ZIP, and verify its contents after extraction, run this command.

```bash
python3 scripts/check.py --package dist
```

For version 1.0.1, attach `dist/idea-to-positioning-1.0.1.zip` to the GitHub release tagged `v1.0.1`. Keep the asset name `idea-to-positioning-1.0.1.zip` and the top-level folder `idea-to-positioning/`.

## Example

The worked example starts with a topic and narrows a broad “anti-AI dependence robot” into a testable “think-first gate.” [Example brief and sources](examples/ai-cognitive-robot/README.md)

The 30% adherence threshold is a **proposed relative test threshold**, not a validated result. The example states the comparator, metric, and calculation:

- Comparator: sticky note / browser prompt;
- Metric: first-answer-before-AI **rate** = events ÷ eligible AI queries in the week; report count and rate;
- Calculation: `(B − A) / A ≥ 0.30` when A > 0; if A = 0, report the percentage-point difference.

## Attribution

- **Author:** Yuyang Gong (龚雨旸) · GitHub: @gyy320603-star
- **Research, drafting, editing, packaging:** Hermes Agent

## Limits

- It cannot replace real observation or user testing.
- It cannot guarantee a good idea.
- It will produce plausible fiction if you skip evidence.
- Human taste makes the final choice.
