# Task execution board

## Active work item

* Objective: Start implementing Phase 7 backlog by adding the workflow transition guard contract.
* Scope boundary: workflow transition template contract, integration example context/template, and focused tests.
* Dependencies: `django_mui/templates/django_mui/examples/integration.html`, `django_mui/views.py`, `tests/test_template_contracts.py`.
* Acceptance criteria:
  - Transition actions can be marked disabled from Django context.
  - Disabled transitions render deterministic reason messaging.
  - Integration example demonstrates enabled and blocked transitions.

## Backlog integration snapshot

- [ ] **In progress**: Add workflow transition guard contract.
- [ ] **Planned**: Add server-rendered table bulk-actions contract.
- [ ] **Planned**: Add navigation + breadcrumb composition contract.
- [x] **Implemented**: Add workflow activity timeline contract.
- [x] **Implemented**: Add advanced list/table server query contract.
- [x] **Implemented**: Add nested navigation section rendering contract.
- [x] **Completed**: Add SSR-first form error summary partial.
- [x] **Completed**: Add server-side tabs navigation template contract.
- [x] **Completed**: Add pagination page-size query helper.
- [x] **Completed**: Document feature parity matrix by maturity level.

## Phase 1 — Plan

- [x] Review current backlog state and select first Phase 7 implementation item.
- [x] Understand existing workflow/template contracts and test patterns.

## Phase 2 — Execute

- [x] Add a reusable workflow transitions partial that supports disabled transitions with reasons.
- [x] Update integration example context/template to show enabled and blocked transitions.
- [x] Add focused template contract tests for workflow guard behavior.

## Phase 3 — Review

- [x] Run targeted tests for workflow/template contracts.
- [x] Run ruff checks and full unittest suite.
- [x] Run code review and security scan.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
