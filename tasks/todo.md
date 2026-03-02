# Task execution board

## Active work item

* Objective: Implement Phase 5 parity documentation matrix.
* Scope boundary: docs-only update focused on parity tiers and backlog mappings.
* Dependencies: `docs/feature-inventory.md`, `docs/implementation-issues.md`, `README.md`.
* Acceptance criteria:
  - parity tiers (`implemented`, `planned`, `out of scope`) are explicit,
  - planned gaps map to open backlog issue drafts,
  - README links to updated parity matrix.

## Phase 5 backlog integration snapshot

- [ ] **Open**: Document feature parity matrix by maturity level (`docs/implementation-issues.md` Phase 5 #4).
- [x] **Completed**: Add SSR-first form error summary partial.
- [x] **Completed**: Add server-side tabs navigation template contract.
- [x] **Completed**: Add pagination page-size query helper.

## Phase 1 — Plan

- [ ] Confirm impacted docs and parity sections.
- [ ] Define matrix columns and canonical tier rules.
- [ ] Identify README references to update.

## Phase 2 — Execute

- [ ] Implement parity matrix update in docs.
- [ ] Map planned gaps to backlog items.
- [ ] Update README links.

## Phase 3 — Review

- [ ] Run targeted checks and record results.
- [ ] Run merge-gate checks and record results.
- [ ] Document risk review and final outcome.
- [ ] Add lessons to `tasks/lessons.md`.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
