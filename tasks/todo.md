# Task execution board

## Active work item

* Objective: Continue backlog by completing the Phase 12 pagination summary and status chip contracts.
* Scope boundary: minimal server-rendered table/list primitive updates (new pagination/status-chip partials, table wiring, integration context/template, CSS, docs/tests).
* Dependencies: `django_mui/templates/django_mui/includes/table.html`, `django_mui/templates/django_mui/includes/pagination_summary.html`, `django_mui/templates/django_mui/includes/status_chip.html`, `django_mui/templates/django_mui/examples/integration.html`, `django_mui/static/django_mui/base.css`, `django_mui/views.py`, `docs/implementation-issues.md`, `tests/test_template_contracts.py`, `tasks/lessons.md`.
* Acceptance criteria:
  - Pagination summary renders from Django context-provided metadata.
  - Status chip renders from Django context-provided label + variant metadata.
  - Existing list/table usage without new metadata remains backward compatible.

## Backlog integration snapshot

- **Completion (selected backlog items)**: 20/20 complete (100%); 0/20 remaining (0%).
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
- [x] **Implemented**: Add server-rendered pagination summary contract.
- [x] **Implemented**: Add server-rendered status chip primitive contract.
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

- [x] Add reusable pagination-summary partial and wire into table integration.
- [x] Add reusable status-chip primitive and integrate with existing row state-badge contract.
- [x] Update integration view/template context for pagination summary metadata.
- [x] Refresh backlog docs and focused contract tests for Phase 12 completion.

## Phase 3 — Review

- [x] Run targeted tests for updated table/template contract areas.
- [x] Run `ruff check .`.
- [x] Run `ruff check . --select S`.
- [x] Run `python -m unittest discover -s tests -p "test_*.py"`.
- [x] Capture updated integration screenshot (`https://github.com/user-attachments/assets/70d9c70e-3db3-4adc-a526-70fd6975390f`).
- [x] Run code review and codeql checker; address actionable findings.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
