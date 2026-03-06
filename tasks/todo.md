# Task execution board

## Active work item

* Objective: Continue backlog by completing the Phase 14 workflow transition history and table selection summary contracts, then quantify remaining porting work.
* Scope boundary: minimal server-rendered workflow/table contract updates (new transition-history/selection-summary partials, integration wiring, CSS, docs/tests).
* Dependencies: `django_mui/templates/django_mui/includes/table.html`, `django_mui/templates/django_mui/includes/table_selection_summary.html`, `django_mui/templates/django_mui/includes/workflow_transition_history.html`, `django_mui/templates/django_mui/examples/integration.html`, `django_mui/static/django_mui/base.css`, `django_mui/views.py`, `docs/implementation-issues.md`, `tests/test_template_contracts.py`, `tasks/lessons.md`.
* Acceptance criteria:
  - Workflow transition history renders from Django context-provided metadata.
  - Table selection summary renders deterministic selected-count + clear-selection affordance from Django context.
  - Existing table/workflow usage without the new metadata remains backward compatible.

## Backlog integration snapshot

- **Completion (selected backlog items)**: 22/24 complete (92%); 2/24 remaining (8%).
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
- [ ] **Selected (current phase)**: Add server-rendered workflow transition history contract.
- [ ] **Selected (current phase)**: Add server-rendered table selection summary contract.
- [x] **Implemented**: Add workflow activity timeline contract.
- [x] **Implemented**: Add advanced list/table server query contract.
- [x] **Implemented**: Add nested navigation section rendering contract.
- [x] **Completed**: Add SSR-first form error summary partial.
- [x] **Completed**: Add server-side tabs navigation template contract.
- [x] **Completed**: Add pagination page-size query helper.
- [x] **Completed**: Document feature parity matrix by maturity level.

## Phase 1 — Plan

- [x] Review open backlog phase and pick the next selected contracts.
- [x] Confirm minimal files/tests to update for workflow/table contract additions.

## Phase 2 — Execute

- [ ] Add reusable workflow-transition-history partial and integrate with workflow section.
- [ ] Add reusable table-selection-summary partial and wire into table integration.
- [ ] Update integration view/template context for transition history + selection summary metadata.
- [ ] Refresh backlog docs and focused contract tests for Phase 14 completion + next-phase remaining-work snapshot.

## Phase 3 — Review

- [ ] Run targeted tests for updated workflow/table template contract areas.
- [ ] Run `ruff check .`.
- [ ] Run `ruff check . --select S`.
- [ ] Run `python -m unittest discover -s tests -p "test_*.py"`.
- [ ] Capture updated integration screenshot for Phase 14 contract additions.
- [ ] Run code review and codeql checker; address actionable findings.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
