# Task execution board

## Active work item

* Objective: Continue Phase 5 backlog by documenting the feature parity matrix with maturity tiers.
* Scope boundary: minimal documentation updates only (`docs/feature-inventory.md` and README link alignment).
* Dependencies: `docs/implementation-issues.md`, `docs/feature-inventory.md`, `README.md`.
* Acceptance criteria:
  - feature inventory includes an explicit maturity matrix (`implemented`, `planned`, `out of scope`),
  - planned gaps in the matrix map to backlog issue drafts,
  - README points readers to the updated parity matrix section.

## Phase 5 backlog integration snapshot

- [x] **Open**: Document feature parity matrix by maturity level.
- [x] **Completed**: Add SSR-first form error summary partial.
- [x] **Completed**: Add server-side tabs navigation template contract.
- [x] **Completed**: Add pagination page-size query helper.

## Phase 1 — Plan

- [x] Confirm open Phase 5 task and impacted docs.
- [x] Define minimal matrix structure and backlog cross-reference requirements.
- [x] Identify README section to align with the updated matrix.

## Phase 2 — Execute

- [x] Add maturity-tier parity matrix section to feature inventory.
- [x] Map planned gaps to issue drafts in `docs/implementation-issues.md`.
- [x] Align README wording/link to the updated matrix section.

## Phase 3 — Review

- [x] Run merge-gate checks and record results.
- [x] Document risk review and final outcome.
- [x] Add lessons to `tasks/lessons.md`.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
