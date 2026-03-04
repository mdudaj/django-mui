# Task execution board

## Active work item

* Objective: Finish the remaining Phase 9 backlog contracts and close the selected backlog queue.
* Scope boundary: minimal server-first contract updates for form widget islands + snackbar bridge, with documentation/tests updates.
* Dependencies: `django_mui/templatetags/django_mui_forms.py`, `django_mui/templates/django_mui/includes/form_field.html`, `django_mui/templates/django_mui/includes/messages.html`, `django_mui/views.py`, `django_mui/templates/django_mui/examples/integration.html`, `docs/implementation-issues.md`, `tests/test_template_contracts.py`.
* Acceptance criteria:
  - Form field adapter supports optional island metadata while preserving server-rendered fallback markup.
  - Messages contract supports optional deterministic snackbar payload serialization without breaking alert rendering.
  - Integration example demonstrates both contracts.
  - `docs/implementation-issues.md` reports selected backlog completion with no remaining items.

## Backlog integration snapshot

- **Completion (selected backlog items)**: 14/14 complete (100%); 0/14 remaining (0%).
- [x] **Implemented**: Add workflow transition guard contract.
- [x] **Implemented**: Add server-rendered table bulk-actions contract.
- [x] **Implemented**: Add navigation + breadcrumb composition contract.
- [x] **Implemented**: Add hybrid form widget islands contract.
- [x] **Implemented**: Add server+snackbar feedback bridge contract.
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

- [x] Review current backlog state and identify the remaining Phase 9 targets.
- [x] Confirm existing template/tag extension points and backlog contract tests.

## Phase 2 — Execute

- [x] Add optional hybrid form widget island metadata contract to form field adapter + integration example.
- [x] Add optional server+snackbar payload bridge contract to messages + integration example.
- [x] Mark Phase 9 backlog as completed and refresh completion snapshot docs.
- [x] Update focused template contract tests for both contracts and backlog state.

## Phase 3 — Review

- [x] Run targeted tests for changed contract areas.
- [x] Run `ruff check .`.
- [x] Run `ruff check . --select S`.
- [x] Run `python -m unittest discover -s tests -p "test_*.py"` and capture integration screenshot.
- [x] Run code review and codeql checker; address findings.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
