# Task execution board

## Active work item

* Objective: Continue Phase 8 backlog by implementing the workflow timeline grouping contract.
* Scope boundary: timeline template/view/example/test updates only; keep existing contracts backward compatible.
* Dependencies: `django_mui/templates/django_mui/includes/timeline.html`, `django_mui/templates/django_mui/examples/integration.html`, `django_mui/views.py`, `tests/test_template_contracts.py`.
* Acceptance criteria:
  - Timeline can render grouped entries from Django context without JavaScript.
  - Empty timeline payloads render a deterministic fallback message.
  - Integration example demonstrates grouped and empty-state timeline payloads.

## Backlog integration snapshot

- [x] **Implemented**: Add workflow transition guard contract.
- [x] **Implemented**: Add server-rendered table bulk-actions contract.
- [x] **Implemented**: Add navigation + breadcrumb composition contract.
- [ ] **In progress**: Add navigation permission-guard contract.
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

- [x] Extend timeline partial to support grouped entries and deterministic empty-state fallback.
- [x] Update integration example to demonstrate grouped and empty timeline payloads.
- [x] Update focused template contract tests for the timeline grouping/empty-state contract.

## Phase 3 — Review

- [x] Run targeted tests for timeline contract updates.
- [x] Run ruff checks and full unittest suite.
- [x] Run code review and security scan.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
