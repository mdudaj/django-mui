# Task execution board

## Active work item

* Objective: Continue Phase 7 backlog by adding the server-rendered table bulk-actions contract.
* Scope boundary: table template contract, integration example context/template behavior, and focused tests.
* Dependencies: `django_mui/templates/django_mui/includes/table.html`, `django_mui/templates/django_mui/examples/integration.html`, `django_mui/views.py`, `tests/test_template_contracts.py`.
* Acceptance criteria:
  - Rows expose selectable state in server-rendered markup.
  - Bulk action submission can be posted with selected IDs.
  - Empty/invalid submissions fail safely with user feedback.

## Backlog integration snapshot

- [x] **Implemented**: Add workflow transition guard contract.
- [x] **Implemented**: Add server-rendered table bulk-actions contract.
- [ ] **In progress**: Add navigation + breadcrumb composition contract.
- [x] **Implemented**: Add workflow activity timeline contract.
- [x] **Implemented**: Add advanced list/table server query contract.
- [x] **Implemented**: Add nested navigation section rendering contract.
- [x] **Completed**: Add SSR-first form error summary partial.
- [x] **Completed**: Add server-side tabs navigation template contract.
- [x] **Completed**: Add pagination page-size query helper.
- [x] **Completed**: Document feature parity matrix by maturity level.

## Phase 1 — Plan

- [x] Review current backlog state and select next Phase 7 implementation item.
- [x] Understand existing table/template contracts and test patterns.

## Phase 2 — Execute

- [x] Add optional table bulk-action form contract with row selection support.
- [x] Update integration example context/template with bulk-action submission feedback.
- [x] Add focused template contract tests for bulk-action behavior.

## Phase 3 — Review

- [x] Run targeted tests for table/template contracts.
- [x] Run ruff checks and full unittest suite.
- [x] Run code review and security scan.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
