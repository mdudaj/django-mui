# Task execution board

## Active work item

* Objective: Render visible Material UI components in the demo dashboard so it no longer appears as plain HTML-only output.
* Scope boundary: minimal, server-first updates that preserve existing templates/contracts while progressively enhancing with MUI islands.
* Dependencies: `django_mui/templates/django_mui/base.html`, `django_mui/static/django_mui/react_islands.js`, `django_mui/views.py`, `django_mui/templates/django_mui/examples/todo_dashboard.html`, `tests/test_template_contracts.py`, `tasks/lessons.md`.
* Acceptance criteria:
  - Base template loads required React/MUI runtime assets for islands.
  - Todo dashboard renders at least one real Material UI component via island mount.
  - Existing todo CRUD server-rendered flows remain functional as fallback behavior.
  - Template contract tests cover new MUI integration hooks.

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

- [x] Confirm requested scope for dashboard MUI rendering enhancement.
- [x] Run baseline validations before edits.
- [x] Confirm minimal implementation files and insertion points for base assets + dashboard island wiring.

## Phase 2 — Execute

- [x] Add runtime island enhancement hooks without requiring external CDN dependencies.
- [x] Add/extend island registration to render Material UI dashboard component(s) with fallback behavior.
- [x] Wire todo dashboard context/template to mount new MUI component while preserving existing CRUD forms.
- [x] Update template contract tests for MUI integration markers.

## Phase 3 — Review

- [x] Run targeted tests for changed template contracts.
- [x] Run `ruff check .`.
- [x] Run `ruff check . --select S`.
- [x] Run `python -m unittest discover -s tests -p "test_*.py"`.
- [x] Capture updated dashboard screenshot for traceability (`https://github.com/user-attachments/assets/e82e6620-ddde-491d-8707-2a39a18c7acd`).
- [ ] Run code review and codeql checker; address actionable findings.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
