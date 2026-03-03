# Task execution board

## Active work item

* Objective: Continue Phase 7 backlog by adding the navigation + breadcrumb composition contract.
* Scope boundary: integration example route-context composition for breadcrumbs/navigation and focused contract tests.
* Dependencies: `django_mui/views.py`, `django_mui/templates/django_mui/examples/integration.html`, `tests/test_template_contracts.py`.
* Acceptance criteria:
  - Breadcrumb current item stays aligned with active navigation state.
  - Base template block contracts remain backward compatible.
  - Accessibility semantics (`aria-current`) remain explicit in both patterns.

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
- [x] Understand existing navigation + breadcrumb contracts and test patterns.

## Phase 2 — Execute

- [x] Add a minimal composed route-context contract for nav sections and breadcrumbs.
- [x] Keep base template usage/backward compatibility unchanged.
- [x] Add focused template contract tests for composed navigation + breadcrumb behavior.

## Phase 3 — Review

- [x] Run targeted tests for navigation/template contracts.
- [x] Run ruff checks and full unittest suite.
- [x] Run code review and security scan.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
