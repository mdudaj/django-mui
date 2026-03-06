# Task execution board

## Active work item

* Objective: Add a demo todo dashboard page with server-rendered CRUD flows and branding-variable showcase.
* Scope boundary: minimal SSR updates within existing example architecture; no unrelated refactors.
* Dependencies: `django_mui/views.py`, `django_mui/urls.py`, example templates, `django_mui/static/django_mui/base.css`, `tests/test_template_contracts.py`, `tasks/lessons.md`.
* Acceptance criteria:
  - Demo dashboard route is reachable from examples and renders a todo-focused dashboard.
  - Dashboard supports create/update/delete/toggle-complete CRUD actions for todos.
  - Dashboard demonstrates branding customization through CSS variable overrides.
  - Template contract tests cover the new demo entry points and core CRUD/branding wiring.

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

- [x] Confirm requested scope for demo todo dashboard + branding showcase.
- [x] Run baseline validations before edits.
- [x] Confirm minimal implementation files and insertion points for demo route/view/template/tests.

## Phase 2 — Execute

- [ ] Add demo dashboard URL and view logic for todo CRUD + branding variable selection.
- [ ] Add/extend example templates with demo dashboard sections and controls.
- [ ] Add minimal stylesheet support for dashboard/branding preview layout.
- [ ] Update template contract tests for new demo dashboard wiring.

## Phase 3 — Review

- [ ] Run targeted tests for changed template contracts.
- [x] Run `ruff check .`.
- [x] Run `ruff check . --select S`.
- [ ] Run `python -m unittest discover -s tests -p "test_*.py"`.
- [ ] Capture updated dashboard screenshot for traceability.
- [ ] Run code review and codeql checker; address actionable findings.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
