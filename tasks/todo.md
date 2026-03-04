# Task execution board

## Active work item

* Objective: Continue Phase 8 backlog by implementing the navigation permission-guard contract.
* Scope boundary: navigation section template/view/test updates only; keep existing contracts backward compatible.
* Dependencies: `django_mui/templates/django_mui/includes/nav_section.html`, `django_mui/views.py`, `tests/test_template_contracts.py`.
* Acceptance criteria:
  - Navigation entries can be flagged unavailable from Django context.
  - Unavailable entries render deterministic fallback semantics.
  - Integration example demonstrates mixed available/unavailable entries.

## Backlog integration snapshot

- [x] **Implemented**: Add workflow transition guard contract.
- [x] **Implemented**: Add server-rendered table bulk-actions contract.
- [x] **Implemented**: Add navigation + breadcrumb composition contract.
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

- [x] Review current backlog state and identify the next minimal Phase 8 implementation target.
- [x] Confirm existing timeline contract files and tests to extend.

## Phase 2 — Execute

- [x] Extend nav section partial to support unavailable entries and deterministic fallback semantics.
- [x] Update integration example context to demonstrate mixed available/unavailable navigation entries.
- [x] Update focused template contract tests for unavailable navigation semantics.

## Phase 3 — Review

- [x] Run targeted tests for navigation contract updates.
- [x] Run ruff checks and full unittest suite.
- [x] Run code review and security scan.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
