# Front-Stage Output

Use when the work is sound but the deliverable is for students, teachers, or other non-AI readers. This changes **presentation**, not the method.

## Reader package

Follow the [workflow](workflow.md) for the underlying positioning work. Use the [output paths](outputs.md) for the front-stage package and working records. Deliver reader-facing documents as PDF or PPTX and provide a short Markdown entry note.

| Reading time | Document | Reader question |
|---|---|---|
| 30 seconds | One-page recommendation | What do you recommend, for whom, and why? |
| 3 minutes | Eight-page proposal | How does it work, and what makes it different? |
| 15 minutes | Evidence and risk | What is sourced, inferred, or still unverified? |

## Chat-style opening

Every human-facing delivery starts with a short note like a normal ChatGPT reply, not a table of contents:

1. what I did;
2. the one-sentence conclusion;
3. how to read it (30 sec / 3 min / 15 min);
4. the biggest thing I have **not** solved;
5. the next cheapest action.

Use the [entry-note template](../templates/read-me-first.md) to mirror the opening in the reader package.

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

Put a one-line legend at the bottom of the page; put the full source table in the evidence-and-risk document.

## One-page structure

1. One-sentence recommendation.
2. Who it is for.
3. What problem it solves.
4. Why now.
5. Biggest risk.
6. Next cheapest test.

No file names, no jargon, no code blocks.

## Eight-page structure

Use the [deck outline](deck-outline.md). In student-facing mode:

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
