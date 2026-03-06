# Task execution board

## Active work item

* Objective: Clarify how much work remains to finish free + pro feature porting scope.
* Scope boundary: docs/tests only; keep implementation backlog and parity language aligned with existing project scope.
* Dependencies: `docs/implementation-issues.md`, `docs/feature-inventory.md`, `tests/test_template_contracts.py`, `tasks/lessons.md`.
* Acceptance criteria:
  - Porting snapshot explicitly answers remaining free + pro scope work.
  - Wording is consistent with feature inventory parity boundaries.
  - Backlog contract test coverage asserts the new wording.

## Backlog integration snapshot

- **Completion (selected backlog items)**: 24/26 complete (92%); 2/26 remaining (8%).
- [x] **Implemented**: Add workflow transition guard contract.
- [x] **Implemented**: Add server-rendered table bulk-actions contract.
- [x] **Implemented**: Add navigation + breadcrumb composition contract.
- [x] **Implemented**: Add hybrid form widget islands contract.
- [x] **Implemented**: Add server+snackbar feedback bridge contract.
- [x] **Implemented**: Add navigation permission-guard contract.
- [x] **Implemented**: Add workflow timeline grouping contract.
- [x] **Implemented**: Add workflow status summary contract.
- [x] **Implemented**: Add server-rendered table column metadata contract.
- [x] **Implemented**: Add server-rendered table row state badge contract.
- [x] **Implemented**: Add server-rendered active-filter summary contract.
- [x] **Implemented**: Add server-rendered workflow transition history contract.
- [x] **Implemented**: Add server-rendered table selection summary contract.
- [x] **Implemented**: Add workflow activity timeline contract.
- [x] **Implemented**: Add advanced list/table server query contract.
- [x] **Implemented**: Add nested navigation section rendering contract.
- [x] **Completed**: Add SSR-first form error summary partial.
- [x] **Completed**: Add server-side tabs navigation template contract.
- [x] **Completed**: Add pagination page-size query helper.
- [x] **Completed**: Document feature parity matrix by maturity level.

## Phase 1 — Plan

- [x] Review current backlog and parity docs to identify remaining free + pro scope work.
- [x] Confirm minimal docs/tests to update for this clarification.

## Phase 2 — Execute

- [x] Update implementation backlog snapshot with explicit free + pro remaining-work wording.
- [x] Update focused template contract assertions for the new wording.

## Phase 3 — Review

- [x] Run targeted tests for updated backlog/template contract areas.
- [x] Run `ruff check .`.
- [x] Run `ruff check . --select S`.
- [x] Run `python -m unittest discover -s tests -p "test_*.py"`.
- [x] Capture updated integration screenshot for traceability (N/A: docs/tests-only change, no UI behavior changed).
- [x] Run code review and codeql checker; address actionable findings.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
