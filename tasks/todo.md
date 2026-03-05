# Task execution board

## Active work item

* Objective: Continue backlog by completing the remaining Phase 10 table column metadata contract.
* Scope boundary: minimal server-rendered table metadata updates (template tag/filter, table partial, example context, CSS, docs/tests).
* Dependencies: `django_mui/templatetags/django_mui_list.py`, `django_mui/templates/django_mui/includes/table.html`, `django_mui/static/django_mui/base.css`, `django_mui/views.py`, `docs/implementation-issues.md`, `tests/test_template_contracts.py`, `tasks/lessons.md`.
* Acceptance criteria:
  - Table columns can declare optional metadata (alignment, emphasis, semantic labels) from Django context.
  - Existing list/table usage without metadata remains backward compatible.
  - Integration example and backlog snapshot/tests reflect completion of selected Phase 10 items.

## Backlog integration snapshot

- **Completion (selected backlog items)**: 16/16 complete (100%); 0/16 remaining (0%).
- [x] **Implemented**: Add workflow transition guard contract.
- [x] **Implemented**: Add server-rendered table bulk-actions contract.
- [x] **Implemented**: Add navigation + breadcrumb composition contract.
- [x] **Implemented**: Add hybrid form widget islands contract.
- [x] **Implemented**: Add server+snackbar feedback bridge contract.
- [x] **Implemented**: Add navigation permission-guard contract.
- [x] **Implemented**: Add workflow timeline grouping contract.
- [x] **Implemented**: Add workflow status summary contract.
- [x] **Implemented**: Add server-rendered table column metadata contract.
- [x] **Implemented**: Add workflow activity timeline contract.
- [x] **Implemented**: Add advanced list/table server query contract.
- [x] **Implemented**: Add nested navigation section rendering contract.
- [x] **Completed**: Add SSR-first form error summary partial.
- [x] **Completed**: Add server-side tabs navigation template contract.
- [x] **Completed**: Add pagination page-size query helper.
- [x] **Completed**: Document feature parity matrix by maturity level.

## Phase 1 — Plan

- [x] Review backlog docs and confirm the remaining executable Phase 10 contract.
- [x] Confirm templates/views/tests to extend for table column metadata behavior.

## Phase 2 — Execute

- [x] Add optional table-column metadata support in shared table rendering contract.
- [x] Wire metadata-enhanced columns into integration example context.
- [x] Refresh backlog snapshot counts and focused template contract tests.

## Phase 3 — Review

- [x] Run targeted tests for changed contract areas.
- [x] Run `ruff check .`.
- [x] Run `ruff check . --select S`.
- [x] Run `python -m unittest discover -s tests -p "test_*.py"` and capture updated integration screenshot.
- [x] Run code review and codeql checker; address actionable findings.
- [x] Screenshot reference for PR: https://github.com/user-attachments/assets/5dfccc4e-445d-476e-b385-e7eb0e0b02d1

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
