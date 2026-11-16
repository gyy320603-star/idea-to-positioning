# Changelog

## 1.0.1 — 2026-11-16

- Split the skill entry point from the detailed positioning workflow. The entry point routes each request to its procedure. [Positioning workflow](references/workflow.md)
- Documented which packaged templates each mode reads and where the resulting files belong in the user's project. [Project output paths](references/outputs.md)
- Added a source-checkout command to check documentation and build the versioned install ZIP. The packaging check extracts the archive, copies it into a temporary Hermes skills directory, and verifies the installed files. [Release instructions](README.md#check-and-package-a-release)

## 1.0.0 — 2026-11-15

- Initial release.
- Personal attribution: author and copyright holder `Yuyang Gong (龚雨旸)`; Hermes Agent credited as collaborator.
- ZIP install shape fixed: version in the ZIP filename, top-level folder `idea-to-positioning/`.
- Full positioning defaults to an 8-page outline; one-page brief is a separate explicit mode.
- Minimal-input mode: topic only, or topic + hypothesis.
- Request-mode routing: full positioning, single grill, campaign, one-pager.
- Evidence thresholds separated: screening (2 sources) vs key claim (3 sources, one non-self-report).
- Universal full-positioning package: 1 + 8 + 1 + 1 + appendix.
- Nine gates from frame to decision.
- Grill protocol with roles, three rounds, stop rules, kill memo.
- Evidence coding and source table.
- Long-run campaign mode.
- Filled example with decision brief, deck outline, grill log, and sources.
- Example evidence downgraded: HKUST is expectation/design research, Brick is a substitute/price anchor, not proof of willingness to pay.
- Primary metric changed to first-answer-before-AI rate, with count and ratio reported; percentage-point difference when baseline is zero.
- Front-stage output layer for students/non-AI readers: `00_先读我.md`, one-page conclusion, 8-page proposal, evidence/risk; optional 5–8 direction idea appendix. Method unchanged.
- macOS and Windows install instructions.
