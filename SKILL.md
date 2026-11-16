---
name: idea-to-positioning
description: "Turn a topic or concept into a defensible position."
version: 1.0.0
author: Yuyang Gong
license: MIT
metadata:
  hermes:
    tags:
      - brand-strategy
      - ideation
      - positioning
      - audience
      - concept-validation
    related_skills:
      - brand-strategy-course-project
      - customer-research
      - competitor-profiling
---

# Idea to Positioning

## When to use

Use when an early-stage project needs one of these:

- find an idea, creative angle, positioning, or target audience;
- turn a vague concept into a testable claim;
- stress-test a concept before making a deck, logo, packaging, or campaign;
- run a "grill me" review that must end in a decision;
- run a multi-batch campaign around one topic, produce many concepts, and select the best (see `references/long-run-mode.md`);
- package a stage-one brand story for non-AI readers: one-page brief, 8-page proposal, evidence/risk;

Do not use for visual identity execution, production CAD, or campaign media buying. Those come after positioning.

## Core stance

- Generate a **portfolio** of directions, then kill most of them. Do not fall in love with the first idea.
- At campaign scale, use a **funnel**, not a pile: many claims → few evidence-backed concepts → one test. Never generate a hundred full decks and pick one.
- A feature gap is not demand. "Competitors do not combine these features" can mean the combination is unnecessary.
- Define **Who by behaviour**, not by demographics. Age, income, and "young people" are sample frames, not personas.
- In a two-person occasion, separate the **initiator** (proposes, plans, carries, invites) from the **companion** (uses, judges, decides whether to return).
- Find a **decision-changing constraint**, not a feature difference. A constraint only counts when it changes time, place, object, or behaviour.
- Keep one promise. A slogan is an invitation or voice; What is the value promise. Never put the slogan in the What slot.
- Label evidence before using it: `[course pXX]`, `[group-confirmed]`, `[observed]`, `[self-report]`, `[inferred]`, `[assumption]`, `[not found]`.
- A grill is a gate, not entertainment. Every grill must delete a sentence, change a decision, or write a kill criterion.

## Inputs

Ask for or infer:

1. Category / track / product area.
2. Assignment or business constraints.
3. Evaluation criteria and deadline.
4. What the group has actually confirmed vs what the agent suggested.
5. Available public evidence: posts, reviews, prices, rules, competitor pages.
6. Course framework, if this is coursework.

If `brand-strategy-course-project` is installed and the user is working on the 《品牌策略与设计管理》 course, load it and use B p47 / A p27 anchors. Course mode adds: 3 persona tags + 3 pains, 2W1H, honeycomb, name + slogan, 3 competitors, SWOT. Page count and 3-minute pitch are packaging choices unless the instructor says otherwise.

## Minimal input mode

The user may give only a topic, or a topic plus a scene/persona hypothesis. Do not require inputs 3, 4, or 5.

| Input | What to do |
|---|---|
| Topic only | Run a public scan, propose 2–3 candidate frames, pick the strongest evidence-backed one, and list the runners-up. |
| Topic + scene/persona | Treat the hypothesis as `[assumption]`; test it against public evidence; keep, narrow, or reject it. |
| Topic + links | Use the links first, then supplement; still record dates and labels. |

Rules:

- Do not invent local interviews, sales, prices, or quotes.
- If the web has no evidence, write `[not found]`; do not fill the gap with a plausible story.
- Default to **provisional**: choose a frame, say why, and show what would change it.
- Ask for at most one clarification if the topic is genuinely ambiguous; otherwise proceed with labelled assumptions.
- Research budget: 8–15 searches, 6–10 extracted sources.
- Screening threshold: two independent sources that agree can advance a concept to the next gate.
- Key-claim threshold: a key claim needs three independent sources, including at least one non-self-report source (official rule, product page, observed behaviour, or dated first-hand account). Fewer than three → label `[assumption]` or `[self-report]`; do not call it proven.
- If three sources conflict, report the conflict instead of averaging it; do not stop at a false consensus.

## Request modes and delivery

Do not send a full deck to a single grill request. Route by request:

| Request | Deliver | Do not deliver |
|---|---|---|
| **Full positioning**: topic only, or topic + scene/persona | `00_DECISION_BRIEF.md` + **8-page** `01_DECK_OUTLINE.md` + `02_GRILL_LOG.md` + `03_SOURCES.md` + appendix | a deck before the claim survives |
| **Single grill**: existing claim/concept | one-page `GRILL.md`: verdict, strongest challenge, evidence status, sentence deleted, decision, next evidence | 8-page deck, unless explicitly asked |
| **Campaign / multi-batch** | `campaign/` folder; report funnel counts; blind review at milestones; deliver only finalists | 100 decks; a winner before blind review |
| **One-pager only** | decision brief + source table | deck |

For a **full positioning** run, use the standard **1 + 8 + 1 + 1 + appendix** package:

```
delivery/
  00_DECISION_BRIEF.md     1 page: verdict, claim, Who, gap, What, How, kill criteria
  01_DECK_OUTLINE.md       8 pages: one question per page
  02_GRILL_LOG.md          1 page: challenges, deletions, decision
  03_SOURCES.md            source table + assumptions + counterexamples
  appendix/
    A_SCAN.md
    B_CONCEPTS.md
    C_SCORECARD.md
    D_EVIDENCE.md
    E_KILL_MEMO.md
```

Course mode adds the course fields to the full-positioning package; it does not change the format. A single-grill request still stops at the grill log.

## Front-stage output

For students and other non-AI readers, add a human-facing layer **without changing the method**. The nine gates, 5–8 directions, grill, and kill criteria stay exactly as they are.

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

Rules:

- PDF/PPTX for the front stage; Markdown stays in `work/`.
- No `claim`, `grill`, `kill criteria`, `[observed]`, or `[assumption]` in the student-facing PDF.
- Use 我们看到的 / 我们的判断 / 还没验证的 / 什么情况下放弃.
- Use green = public source/verified; yellow = inference/single source; grey = assumption.
- The optional idea appendix shows the existing 5–8 directions; it does **not** add a 48-seed divergence method.

Use `references/front-stage-output.md`.

## Workflow: nine gates

### Gate 0 — Frame

Write one page:

- category and scene;
- who has the job-to-be-done;
- constraints (rules, budget, body, transport, storage, course limits);
- evaluation criteria;
- confirmed decisions;
- open questions;
- source labels for each.

Output: `01_frame.md`.

Stop if you cannot state the scene in one sentence. A track is not a topic; "light outdoor" must shrink to a scene and a product.

### Gate 1 — Scan

Scan five lenses:

| Lens | What to look for |
|---|---|
| Rules | official text, date, jurisdiction, enforcement, exceptions |
| Rituals | what people already do in this occasion, in what order |
| Substitutes | the cheapest commodity or behaviour that already solves it |
| Workarounds | tape, bags, borrowed items, timing tricks, asking a friend |
| Complaints | reviews, comments, posts, repeated phrases, negative cases |

For each item record source, date, behaviour, and whether it is observation or inference. For rules, pull the actual text; do not design around a folk version.

Output: `02_opportunity_map.md`.

### Gate 2 — Diverge

Produce 5–8 directions. Each must be a falsifiable claim:

> For **[specific audience]**, in **[specific scene/frequency]**, existing **[substitute]** causes **[measurable loss]**; the concept uses **[mechanism]** to reduce it to **[metric]**, while net added weight / volume / cost stays below **[threshold]**.

Use constraint remix, not free brainstorming:

- remove a constraint (no pegs, no electricity, no table);
- translate a constraint (indoor ritual to outdoor, restaurant service to park);
- combine two objects (mat + bag, invitation + shade);
- change the role (buyer, host, companion, cleaner);
- change the moment (before, during, after; arrival, meal, return).

Output: `03_concepts.md`.

### Gate 3 — Score and kill

Score each direction 1–5 on:

- specificity of scene;
- strength of evidence;
- difference from substitutes;
- feasibility / structure / cost;
- brand potential;
- course or brief fit.

Pre-register kill criteria before research. For every killed direction write a **kill memo**:

- what was killed;
- which evidence killed it;
- what reusable insight remains;
- what would bring it back.

Output: `04_scorecard.md`, `05_kill_memo.md`.

### Gate 4 — Observe

Use public secondary material or real behaviour. Do not invent interviews.

Code each piece of evidence:

- `[observed]` — you can see the behaviour in a post/photo/video/price page;
- `[self-report]` — the author says they do/want it, but you did not see it;
- `[inferred]` — your interpretation;
- `[assumption]` — no evidence yet;
- `[not found]` — searched, did not find.

Look for:

- frequency and last real occasion;
- what they carried, who carried it, who paid, who cleaned;
- what they changed because of the constraint;
- negative cases and counter-segments;
- whether the evidence comes from the same relationship context (stranger vs close friend vs family).

Output: `06_evidence.md`.

If the target behaviour does not occur in the evidence, do not build a prototype. Pivot or kill.

### Gate 5 — Position

Write the positioning canvas:

- **Who**: behaviour + relationship + occasion + frequency. Name initiator and companion separately.
- **Existing substitute**: cheapest commodity or current behaviour, with cost/time/weight.
- **Gap**: decision-changing constraint, not a feature gap.
- **What**: one promise, <=15 Chinese characters in course mode; not a product description; not a slogan.
- **How**: invitation, ritual, or mechanism that reaches the initiator and gives the companion a reason to come/return.
- **Proof**: three reasons or evidence points.
- **Kill criteria**: what result would make you abandon this.

Output: `07_positioning.md`.

### Gate 6 — Prove

- Three direct competitors or alternatives: price, positioning, visual/CMF, experience gap; source URL and retrieval date.
- SWOT.
- A "what would falsify this" paragraph.
- Separate observed facts from inference; never write "no one does this" as an absolute.

Output: `08_proof.md`.

### Gate 7 — Package

Only for a full-positioning request. Default to the 8-page outline. Use a one-page brief only when the user explicitly asks for one page. A single-grill request stops at Gate 8 and delivers a one-page grill log, not a deck. One page answers one question. Label every important claim. Include a "known unknowns" box.

Default 8-page map:

```
P1 cover: brand + one-line promise + invitation
P2 context/constraint/track
P3 audience: behaviours and pains
P4 2W1H or positioning canvas
P5 brand idea / six dimensions
P6 competitors + SWOT
P7 journey + weakest touchpoint
P8 next steps + validation
```

Output: `09_deck_outline.md`.

### Gate 8 — Grill

Run a claim grill, an evidence grill, and a deck grill. Use `references/grill-protocol.md`.

Minimum rules:

- no claim, no grill;
- every question must cite a source or a slide;
- allow "I don't know"; downgrade to `[assumption]`;
- each round ends with continue / narrow / pivot / kill;
- maximum three rounds;
- require one sentence to delete and one decision to change.

Output: `10_grill.md` and `templates/decision-log.md` filled in.

If the request is grill-only, stop here and deliver `GRILL.md`; do not build a deck.

### Gate 9 — Decide

Write the decision:

- continue, narrow, pivot, or kill;
- the one claim that survives;
- the next cheapest evidence;
- owner and date;
- what would change the decision.

Output: `11_decision.md`.

## Grill shape

When the user says "grill me", do not default to agreement. Start with the strongest disconfirming question. Use this shape:

1. Verdict: what survives, what does not.
2. The weakest link in the current claim.
3. Evidence required to keep it alive.
4. Kill criteria / when to abandon.
5. If useful, a more reasonable reframe.

Do not invent local interviews. Ask for real observations, weights, photos, screenshots, or test results.

## Answer shape

- Start with a one-sentence verdict or current-gate judgment.
- Follow with a table or numbered steps, each with an output and a gate.
- End with one concrete next action and a file path.
- In grill mode, end with the minimum evidence needed for the next round, not encouragement.
- In campaign mode, report the funnel counts and the current phase; do not declare a winner before the blind review.
- In front-stage mode, start with a chat-style note: what you did, the one-sentence conclusion, how to read it, the biggest unknown, and the next action. Mirror it in `00_先读我.md`.

## Guardrails

- Never fabricate interviews, sales, prices, market share, or quotes.
- Do not call a demographic band a Who.
- Do not treat a chosen track as a chosen product.
- Do not treat a mention as a decision-changing constraint.
- Do not use a stranger-buddy post as evidence for a close-friend relationship, or a family post as evidence for a two-friend occasion.
- Do not put a slogan in the What slot.
- Do not start logo, VI, packaging, or campaign before positioning survives.
- Do not make absolute claims ("no one does this", "everyone wants this") from a limited search.
- Do not let a grill end without a decision.
- A design workshop, testimonial, or price page proves expectation, existence, or a price anchor — not effect or willingness to pay. Label it accordingly.
- Prefer rate metrics over raw counts. If the baseline is zero, relative lift is undefined; report the percentage-point difference and both raw counts and rates.

## References

- `references/grill-protocol.md` — roles, rounds, stop rules, output.
- `references/question-bank.md` — audience, substitute, weight, evidence, abandonment, deck questions.
- `references/evidence-coding.md` — source labels, evidence transfer errors, quote rules.
- `references/positioning-canvas.md` — fill-in canvas and examples.
- `references/deck-outline.md` — 8-page deck map and page rules.
- `references/minimal-input-mode.md` — topic-only input, research budget, source hierarchy.
- `references/long-run-mode.md` — multi-batch campaign, funnel, blind tournament, stop rules.
- `references/front-stage-output.md` — one-page/8-page/evidence-risk layer for non-AI readers.
- `templates/claim-one-pager.md` — one-page claim template.
- `templates/concept-card.md` — one-page concept card for a campaign database.
- `templates/decision-brief.md` — universal one-page delivery brief.
- `templates/read-me-first.md` — chat-style entry page for non-AI readers.
- `templates/kill-memo.md` — kill memo template.
- `templates/decision-log.md` — grill decision log.
- `templates/source-table.md` — sources, assumptions, counterexamples.

## Examples

- `examples/ai-cognitive-robot/` — filled decision brief, deck outline, grill log, and source table from a topic-only run. The 30% adherence threshold is a proposed relative test threshold, not a validated result; the example states the comparator, metric, and calculation.

## Worked pattern (short)

A failed hard-shell picnic box was reduced to a connector, then killed by a two-ziplock baseline. The reusable insight was not the box; it was the **initiator/companion** distinction. A later direction used a park rule (pegs/ropes banned, tents allowed) plus the initiator's hosting job to form a no-pegs/no-ropes two-person shade promise. The deck was built only after the claim survived; the failed concept stayed in the kill memo.

Use the pattern, not the product.

## Packaging this skill

- Keep the ZIP filename versioned, but fix the top-level folder inside the archive to `idea-to-positioning/`; install commands must use that exact name.
- Test the archive by extracting it and running the README copy command; do not trust the folder name by eye.
- Keep the human author/copyright holder separate from the tool credit; Hermes Agent is a collaborator, not the copyright holder.
- Do not ship `.git`, caches, or absolute paths; run a ZIP integrity test and a reference check.
- Keep README, SKILL.md, references, and the filled example on the same thresholds and delivery modes.
