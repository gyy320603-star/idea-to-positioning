# Front-Stage Output

Use when the work is sound but the deliverable is for students, teachers, or other non-AI readers. This changes **presentation**, not the method.

## What stays the same

- Nine gates.
- 5–8 directions in Gate 2.
- Evidence coding, grill, kill criteria, decision.
- The workbench files in `work/`.

## Front stage

```
delivery/
  00_先读我.md             1 screen: chat-style entry, how to read, biggest unknown
  01_ONE_PAGE.pdf          1 page: recommendation, who, why, biggest risk, next step
  02_8PAGE_PROPOSAL.pdf    the selected direction, one question per page
  03_EVIDENCE_RISK.pdf     what we saw / what we inferred / what is unverified
  04_IDEA_APPENDIX.pdf     optional: the 5–8 directions already produced in Gate 2
```

Back stage:

```
work/
  A_SCAN.md
  B_CONCEPTS.md
  C_SCORECARD.md
  D_EVIDENCE.md
  E_KILL_MEMO.md
```

PDF/PPTX for the front stage. Markdown only for the workbench or the agent.

## Three reading layers

| Layer | File | Reader question |
|---|---|---|
| 30 seconds | `01_ONE_PAGE.pdf` | What do you recommend, for whom, and why? |
| 3 minutes | `02_8PAGE_PROPOSAL.pdf` | How does it work, and what makes it different? |
| 15 minutes | `03_EVIDENCE_RISK.pdf` | What is sourced, inferred, or still unverified? |

The optional `04_IDEA_APPENDIX.pdf` shows the directions that already exist; it does not add a new divergence method.

## Chat-style opening

Every human-facing delivery starts with a short note like a normal ChatGPT reply, not a table of contents:

1. what I did;
2. the one-sentence conclusion;
3. how to read it (30 sec / 3 min / 15 min);
4. the biggest thing I have **not** solved;
5. the next cheapest action.

Mirror that note in `00_先读我.md`. Use `templates/read-me-first.md`.

The `.md` is the front door for people who like reading in chat/file form. The PDFs are the main delivery for people who do not open Markdown.

## Plain-language mapping

| Internal | Front stage |
|---|---|
| claim | 核心判断 |
| grill | 我们怎么质疑自己 |
| kill criteria | 什么情况下放弃 |
| `[observed]` | 我们看到的 |
| `[self-report]` | 对方自述 |
| `[inferred]` | 我们的推断 |
| `[assumption]` | 还没验证的假设 |
| `[not found]` | 没查到 |
| deck outline | 八页汇报大纲 |
| appendix | 依据与风险 |

## Confidence colours

- **Green**: public source or verified.
- **Yellow**: one source or inference.
- **Grey**: assumption / not verified.

Put a one-line legend at the bottom of the page; put the full source table in `02_EVIDENCE_RISK.pdf`.

## One-page structure

1. One-sentence recommendation.
2. Who it is for.
3. What problem it solves.
4. Why now.
5. Biggest risk.
6. Next cheapest test.

No file names, no jargon, no code blocks.

## Eight-page structure

Use `references/deck-outline.md`. In student-facing mode:

- larger headings, shorter lines;
- one question per page;
- speaker notes separate from slide text;
- no `[observed]` / `[assumption]` tags on the slide;
- source names and dates in the footer, full table in the evidence file.

## Idea appendix (optional)

If the user wants to see the breadth, include the 5–8 directions already generated in Gate 2:

- one line each;
- who/scene;
- mechanism;
- why it is interesting;
- what would kill it.

This is an output of the existing method, not a 48-seed divergence process.

## Rules

- Do not change the method to fit the format.
- Do not hide uncertainty; translate it.
- Do not put a 30-page appendix in front of the one-page answer.
- Do not make the reader learn `claim`, `grill`, or `kill criteria` to understand the recommendation.
