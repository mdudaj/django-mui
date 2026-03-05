# Task execution board

## Active work item

* Objective: Continue backlog by completing the Phase 13 table-toolbar actions and workflow audit banner contracts.
* Scope boundary: minimal server-rendered table/workflow contract updates (new toolbar/audit partials, table/workflow wiring, integration context/template, CSS, docs/tests).
* Dependencies: `django_mui/templates/django_mui/includes/table.html`, `django_mui/templates/django_mui/includes/table_toolbar_actions.html`, `django_mui/templates/django_mui/includes/workflow_audit_banner.html`, `django_mui/templates/django_mui/examples/integration.html`, `django_mui/static/django_mui/base.css`, `django_mui/views.py`, `docs/implementation-issues.md`, `tests/test_template_contracts.py`, `tasks/lessons.md`.
* Acceptance criteria:
  - Table toolbar actions render from Django context-provided metadata.
  - Workflow audit banner renders from Django context-provided metadata.
  - Existing table/workflow usage without new metadata remains backward compatible.

## Backlog integration snapshot

- **Completion (selected backlog items)**: 22/22 complete (100%); 0/22 remaining (0%).
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
- [x] **Implemented**: Add server-rendered table toolbar actions contract.
- [x] **Implemented**: Add server-rendered workflow audit banner contract.
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

- [x] Add reusable table-toolbar actions partial and wire into table integration.
- [x] Add reusable workflow audit banner partial and integrate with workflow section.
- [x] Update integration view/template context for toolbar actions + workflow audit metadata.
- [x] Refresh backlog docs and focused contract tests for Phase 13 completion.

## Phase 3 — Review

- [x] Run targeted tests for updated table/workflow template contract areas.
- [x] Run `ruff check .`.
- [x] Run `ruff check . --select S`.
- [x] Run `python -m unittest discover -s tests -p "test_*.py"`.
- [x] Capture updated integration screenshot (`https://github.com/user-attachments/assets/b80dba47-c089-49c7-a848-e3974dbfb80d`).
- [x] Run code review and codeql checker; address actionable findings.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
