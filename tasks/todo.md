# Task execution board

## Active work item

* Objective: Finish the two remaining Phase 15 OSS parity contracts (workflow SLA summary + table saved-view metadata).
* Scope boundary: minimal SSR template/view/test/docs updates only; preserve backward-compatible optional rendering.
* Dependencies: `django_mui/views.py`, integration + include templates, `django_mui/static/django_mui/base.css`, `docs/implementation-issues.md`, `tests/test_template_contracts.py`, `tasks/lessons.md`.
* Acceptance criteria:
  - Workflow SLA summary contract is implemented via reusable include + integration context/template wiring.
  - Table saved-view metadata contract is implemented via reusable include + integration context/template wiring.
  - Existing integration/table/workflow rendering remains backward compatible when metadata is absent.
  - Backlog snapshot and contract tests reflect completed Phase 15 work.

## Backlog integration snapshot

- **Completion (selected backlog items)**: 26/26 complete (100%); 0/26 remaining (0%).
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
- [x] **Implemented**: Add server-rendered workflow SLA breach summary contract.
- [x] **Implemented**: Add server-rendered table saved-view metadata contract.

## Phase 1 — Plan

- [x] Confirm backlog scope and remaining Phase 15 contracts.
- [x] Run baseline validations before edits.
- [x] Confirm minimal implementation files and insertion points for both contracts.

## Phase 2 — Execute

- [x] Add workflow SLA summary include and wire it into integration template/view context.
- [x] Add table saved-view metadata include and wire it into table integration flow.
- [x] Extend stylesheet with minimal classes for new includes.
- [x] Update template contract tests for new includes and integration wiring.
- [x] Update implementation backlog docs to mark Phase 15 completed.

## Phase 3 — Review

- [x] Run targeted tests for changed template contracts.
- [x] Run `ruff check .`.
- [x] Run `ruff check . --select S`.
- [x] Run `python -m unittest discover -s tests -p "test_*.py"`.
- [x] Capture updated integration screenshot for traceability (`https://github.com/user-attachments/assets/9609dc33-61b3-4732-9934-72dc97b18ce6`).
- [x] Run code review and codeql checker; address actionable findings.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
