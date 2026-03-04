# Task execution board

## Active work item

* Objective: Clarify how much work remains to complete the current porting backlog.
* Scope boundary: planning documentation and backlog contract test updates only.
* Dependencies: `docs/implementation-issues.md`, `tests/test_template_contracts.py`.
* Acceptance criteria:
  - `docs/implementation-issues.md` includes an explicit completion snapshot for selected backlog items.
  - Snapshot states how many selected backlog contracts remain open.
  - Backlog contract tests assert the completion snapshot text.

## Backlog integration snapshot

- **Completion (selected backlog items)**: 12/14 complete (85.7%); 2/14 remaining (14.3%).
- [x] **Implemented**: Add workflow transition guard contract.
- [x] **Implemented**: Add server-rendered table bulk-actions contract.
- [x] **Implemented**: Add navigation + breadcrumb composition contract.
- [ ] **Planned**: Add hybrid form widget islands contract.
- [ ] **Planned**: Add server+snackbar feedback bridge contract.
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

- [x] Review current backlog state and identify the next minimal continuation target.
- [x] Confirm backlog contract tests that track completion status text.

## Phase 2 — Execute

- [x] Add explicit selected-backlog completion snapshot to implementation planning docs.
- [x] Update focused template contract tests for completion snapshot text.

## Phase 3 — Review

- [x] Run targeted tests for backlog contract updates.
- [x] Run ruff checks and full unittest suite.
- [x] Run code review and security scan.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
