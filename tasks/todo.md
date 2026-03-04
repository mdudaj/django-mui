# Task execution board

## Active work item

* Objective: Continue backlog progression by opening the next actionable phase after Phase 9 completion.
* Scope boundary: documentation + contract-test updates only (no feature implementation changes).
* Dependencies: `docs/implementation-issues.md`, `tests/test_template_contracts.py`, `tasks/lessons.md`.
* Acceptance criteria:
  - `docs/implementation-issues.md` opens a new actionable phase with at least two selected tasks.
  - Porting completion snapshot reflects completed vs remaining selected backlog items.
  - Template contract tests validate the updated backlog status text.

## Backlog integration snapshot

- **Completion (selected backlog items)**: 14/16 complete (88%); 2/16 remaining (12%).
- [x] **Implemented**: Add workflow transition guard contract.
- [x] **Implemented**: Add server-rendered table bulk-actions contract.
- [x] **Implemented**: Add navigation + breadcrumb composition contract.
- [x] **Implemented**: Add hybrid form widget islands contract.
- [x] **Implemented**: Add server+snackbar feedback bridge contract.
- [x] **Implemented**: Add navigation permission-guard contract.
- [x] **Implemented**: Add workflow timeline grouping contract.
- [x] **Implemented**: Add workflow activity timeline contract.
- [x] **Implemented**: Add advanced list/table server query contract.
- [x] **Implemented**: Add nested navigation section rendering contract.
- [x] **Completed**: Add SSR-first form error summary partial.
- [x] **Completed**: Add server-side tabs navigation template contract.
- [x] **Completed**: Add pagination page-size query helper.
- [x] **Completed**: Document feature parity matrix by maturity level.

## Phase 1 — Plan

- [x] Review backlog docs and identify the next phase needed to continue execution.
- [x] Confirm tests that enforce backlog documentation contract text.

## Phase 2 — Execute

- [x] Open a new Phase 10 backlog section with selected parallel tasks.
- [x] Refresh completion snapshot counts and remaining-contract text.
- [x] Update focused template contract tests for the new open/completed phase state.

## Phase 3 — Review

- [x] Run targeted tests for changed contract areas.
- [x] Run `ruff check .`.
- [x] Run `ruff check . --select S`.
- [x] Run `python -m unittest discover -s tests -p "test_*.py"` (no UI markup changes required screenshot refresh).
- [x] Run code review and codeql checker; addressed actionable findings.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
