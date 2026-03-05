# Task execution board

## Active work item

* Objective: Continue backlog by completing the Phase 11 table row state badge and active-filter summary contracts.
* Scope boundary: minimal server-rendered table/list contract updates (table partial, new filter summary partial, integration context/template, CSS, docs/tests).
* Dependencies: `django_mui/templates/django_mui/includes/table.html`, `django_mui/templates/django_mui/includes/active_filter_summary.html`, `django_mui/templates/django_mui/examples/integration.html`, `django_mui/static/django_mui/base.css`, `django_mui/views.py`, `docs/implementation-issues.md`, `tests/test_template_contracts.py`, `tasks/lessons.md`.
* Acceptance criteria:
  - Row state badge metadata can be provided from Django context.
  - Active filters can render deterministic summary labels + reset link from Django context.
  - Existing list/table usage without new metadata remains backward compatible.

## Backlog integration snapshot

- **Completion (selected backlog items)**: 18/18 complete (100%); 0/18 remaining (0%).
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
- [x] **Implemented**: Add workflow activity timeline contract.
- [x] **Implemented**: Add advanced list/table server query contract.
- [x] **Implemented**: Add nested navigation section rendering contract.
- [x] **Completed**: Add SSR-first form error summary partial.
- [x] **Completed**: Add server-side tabs navigation template contract.
- [x] **Completed**: Add pagination page-size query helper.
- [x] **Completed**: Document feature parity matrix by maturity level.

## Phase 1 — Plan

- [x] Review open backlog phase and pick the next selected contracts.
- [x] Confirm minimal files/tests to update for table/list contract additions.

## Phase 2 — Execute

- [x] Add row state badge rendering contract to the reusable table partial.
- [x] Add reusable active-filter summary partial and wire into table integration.
- [x] Update integration view/template context for badge + filter summary metadata.
- [x] Refresh backlog docs and focused contract tests for Phase 11 completion.

## Phase 3 — Review

- [x] Run targeted tests for updated table/template contract areas.
- [x] Run `ruff check .`.
- [x] Run `ruff check . --select S`.
- [x] Run `python -m unittest discover -s tests -p "test_*.py"`.
- [x] Capture updated integration screenshot (`https://github.com/user-attachments/assets/1fa7ce87-055f-46e2-b7ec-ab8983ddc2c0`).
- [x] Run code review and codeql checker; address actionable findings.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
