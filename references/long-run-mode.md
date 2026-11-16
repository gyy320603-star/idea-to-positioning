# Long-Run Mode

Use when the user wants to stay on one topic for multiple batches, produce many concepts, and choose the best. The unit is a **campaign**, not one answer.

## Principle

Output volume belongs at the **top** of the funnel, not the bottom.

```
100 claims → 25 deduped → 12 screened → 6 evidence-backed
→ 5 one-pagers → 3 deep dives → 1–2 tests → 1 decision
```

Do not generate a hundred polished decks and pick one. Generate cheap claims, kill early, deepen only survivors.

## Modes

| Mode | Duration | Output |
|---|---|---|
| Sprint | 2–3 days | 48 raw → 12 shortlist → 5 one-pagers → 1 deep dive |
| Campaign | 2–4 weeks | 80–100 raw → 20 shortlist → 10 evidence → 5 one-pagers → 3 deep dives → 1–2 tests |
| Continuous | weekly batches | 10–15 new concepts/week; monthly blind review; quarterly kill review |

Do not run a campaign 24/7. Marginal quality falls, cost rises, and the output becomes homogeneous. Stop when the stop rules fire.

## Campaign folder

Create this structure in the project campaign directory specified by [output paths](outputs.md).

```
campaign/
  DOSSIER.md          topic, constraints, rubric, confirmed decisions
  RUBRIC.md           scoring criteria and weights
  concepts.jsonl      one concept per line
  batches/            raw output per batch
  shortlist/          selected concepts
  deep_dives/         one-pagers and deck outlines
  decisions/          decision log per round
  kill_memos/         why concepts died and what insight remains
  sources/            source tables and assumption logs
```

Use files as memory. A long campaign will exceed one context window; the dossier and concept database are what survive.

## Phase table

| Phase | Action | Output | Gate |
|---|---|---|---|
| 0 | Write dossier and rubric | `DOSSIER.md`, `RUBRIC.md` | scene can be stated in one sentence |
| 1 | Six lens batches | 40–60 raw concepts | each concept has a falsifiable claim |
| 2 | Dedupe and cluster | 20–30 concepts | duplicates merged by claim, not title |
| 3 | Cheap screen | 12 shortlist | kill criteria written first |
| 4 | Evidence sprint | 6 concepts | 2–3 sources per concept; no source = assumption |
| 5 | One-pagers | 5 concepts | Who / substitute / gap / What / How filled |
| 6 | Blind tournament | 3 finalists | anonymized pairwise review |
| 7 | Deep dives | 2–3 concepts | 8-page outline or rough prototype |
| 8 | Behaviour test | 1–2 tests | real choice, not stated preference |
| 9 | Decide | 1 direction | continue / narrow / pivot / kill |

## Concept card

Every concept is one card, not an essay. Minimum fields:

- ID and batch;
- one-line falsifiable claim;
- Who by behaviour;
- scene and frequency;
- existing substitute;
- mechanism;
- evidence status;
- score;
- status: raw / shortlist / evidence / one-pager / finalist / killed;
- kill reason or next test.

Use the [concept-card template](../templates/concept-card.md) as input when creating campaign records.

## Divergence lenses

Run batches by lens, not by “think of more ideas”.

| Lens | Question |
|---|---|
| Rules | What rule makes the current behaviour fail? |
| Rituals | What sequence do people already follow? |
| Substitutes | What is the cheapest commodity or do-nothing option? |
| Workarounds | What DIY fix already exists? |
| Complaints | What do people repeatedly complain about? |
| Roles | Who initiates, accompanies, cleans, pays? |

Change the director constraint per batch: no app, no electricity, under 50, physical object only, service only, two-person only, anti-efficiency only, friend-only, etc. **Diversity comes from constraints, not from asking for “more creative” ideas.**

## Cheap screen

Kill before polishing:

- Can it be stated in one sentence?
- Is there observed behaviour, not just a stated preference?
- Is it different from the cheapest substitute?
- Can a rough prototype exist in two weeks?
- Is there brand potential beyond a feature?
- Is there a privacy, safety, or regulatory blocker?

Every kill gets a kill memo: what died, which evidence killed it, what reusable insight remains, what would bring it back.

## Evidence sprint

For each shortlisted concept, spend a fixed budget:

- 1 behaviour/demand source;
- 1 substitute/competitor source;
- 1 counterexample;
- 2–3 sources maximum.

If the evidence is not there, downgrade to `[assumption]`. Do not write a deck to hide the gap.

## Blind tournament

Do not let the generator judge its own output.

- Remove names, authors, and brand styling.
- Three judges: strategist, designer, skeptic.
- Pairwise comparison: “which is more specific / evidence-backed / different / feasible?”
- Keep dissent; do not average it away.
- Human makes the final choice.

Score **confidence** and **upside** separately. A high-average idea can still be less interesting than a high-upside one with a clear test.

## Portfolio selection

Do not pick one point estimate. Pick a portfolio:

- **Safe bet**: high confidence, moderate upside.
- **Adjacent bet**: medium confidence, high upside.
- **Wild bet**: low confidence, very high upside or learning value.

Execute one; keep one as backup. Do not execute all three.

## Stop rules

- 80% of new concepts map to existing clusters → stop divergence.
- Top 3 survive two evidence checks and one human review → stop screening, deepen.
- Time or budget is exhausted → decide with what exists.
- Two batches produce no new insight → change lens, not volume.
- You feel unable to kill a concept → write the kill memo first, then decide.

## Budget

```
60% cheap divergence
30% evidence and deepening
10% packaging
```

Do not reverse it. A beautiful deck built before evidence is the most expensive way to be wrong.

## Anti-homogenization

- Different lenses and constraints.
- Different director personas.
- Cross-industry analogies.
- Extreme users and negative cases.
- Human-seeded “weird references” the model must vary around.

## Anti-self-preference

- Separate generation from judging.
- Blind the concepts.
- Use multiple judges.
- Prefer behaviour evidence over rhetorical quality.
- Keep a skeptic whose job is to argue for kill.

## Human checkpoints

At minimum:

1. after the first 20–30 concepts, choose which clusters to deepen;
2. after the evidence sprint, choose which 5 deserve one-pagers;
3. after the blind tournament, choose which 1–2 to test.

Do not automate taste. Automate the bookkeeping and the first pass.

## Minimum pilot

If the user wants to test the mode cheaply:

```
3 batches × 10 concepts = 30
→ dedupe to 12
→ evidence sprint on 6
→ 3 one-pagers
→ blind review
→ 1 deep dive
```

This is enough to see whether volume improves selection, without producing an unusable pile.

## What this mode is not

- Not 24/7 autonomous ideation.
- Not 100 full decks.
- Not a substitute for human taste.
- Not a reason to skip evidence.
