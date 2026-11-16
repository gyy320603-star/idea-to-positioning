# idea-to-positioning

**Turn a topic or concept into a defensible position.**

Version 1.0.0 · MIT · Author: Yuyang Gong (龚雨旸)

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

## Front-stage output

For students, teachers, and other non-AI readers, add a readable front stage without changing the method:

```
delivery/
  00_先读我.md             1 screen: chat-style entry, how to read, biggest unknown
  01_ONE_PAGE.pdf          1 page: recommendation, who, why, biggest risk
  02_8PAGE_PROPOSAL.pdf    the selected direction, one question per page
  03_EVIDENCE_RISK.pdf     what we saw / what we inferred / what is unverified
  04_IDEA_APPENDIX.pdf     optional: the 5–8 directions already produced in Gate 2
work/
  A_SCAN.md ... E_KILL_MEMO.md
```

The chat-style entry is not a table of contents. It says what was done, the one-sentence conclusion, how to read it (30 sec / 3 min / 15 min), what is still unsolved, and the next cheapest action.

No `claim`, `grill`, `kill criteria`, `[observed]`, or `[assumption]` in the student-facing PDF. Use 我们看到的 / 我们的判断 / 还没验证的 / 什么情况下放弃.

PDF/PPTX for the front stage; Markdown only for the workbench.

## Full package

```
delivery/
  00_DECISION_BRIEF.md     1 page: verdict, claim, Who, gap, What, How, kill criteria
  01_DECK_OUTLINE.md       8 pages: one question per page
  02_GRILL_LOG.md          1 page: challenges, deletions, decision
  03_SOURCES.md            sources, assumptions, counterexamples
appendix/
  A_SCAN.md
  B_CONCEPTS.md
  C_SCORECARD.md
  D_EVIDENCE.md
  E_KILL_MEMO.md
```

## Workflow

| Gate | Action | Output |
|---|---|---|
| 0 Frame | Category, scene, constraints, evaluation criteria, confirmed vs assumed | `01_frame.md` |
| 1 Scan | Rules, rituals, substitutes, workarounds, complaints | `02_opportunity_map.md` |
| 2 Diverge | 5–8 concepts, each a falsifiable claim | `03_concepts.md` |
| 3 Score/Kill | Score, pre-register kill criteria, write kill memos | `04_scorecard.md`, `05_kill_memo.md` |
| 4 Observe | Public evidence or real behaviour; label every claim | `06_evidence.md` |
| 5 Position | Who by behaviour, substitute, gap, one promise, How | `07_positioning.md` |
| 6 Prove | Competitors, SWOT, “what would falsify this” | `08_proof.md` |
| 7 Package | 8-page outline by default; one page only on explicit request | `09_deck_outline.md` |
| 8 Grill | Claim, evidence, deck; max three rounds | `10_grill.md` |
| 9 Decide | Continue / narrow / pivot / kill | `11_decision.md` |

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

The ZIP contains a single top-level folder named `idea-to-positioning/`. Unzip it first, then copy that folder.

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

## Files

```
SKILL.md
README.md
LICENSE
CHANGELOG.md
CONTRIBUTORS.md
references/
  grill-protocol.md
  question-bank.md
  evidence-coding.md
  positioning-canvas.md
  deck-outline.md
  minimal-input-mode.md
  long-run-mode.md
  front-stage-output.md
templates/
  claim-one-pager.md
  concept-card.md
  decision-brief.md
  decision-log.md
  kill-memo.md
  read-me-first.md
  source-table.md
examples/
  ai-cognitive-robot/
    README.md
    00_DECISION_BRIEF.md
    01_DECK_OUTLINE.md
    02_GRILL_LOG.md
    03_SOURCES.md
```

## Example

`examples/ai-cognitive-robot/` is a filled topic-only run. It narrows a broad “anti-AI dependence robot” into a testable “think-first gate.”

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
