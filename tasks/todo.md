# Task execution board

## Active work item

* Objective: Implement Phase 6 selected parallel tasks (timeline + multi-filter).
* Scope boundary: timeline partial, multi-filter helpers, template tag, tests, CSS.
* Dependencies: `django_mui/list_query.py`, `django_mui/templatetags/django_mui_list.py`, templates, CSS.
* Acceptance criteria:
  - Timeline renders event entries from Django context without JavaScript.
  - Event entries support semantic timestamps and status labels.
  - Integration example demonstrates timeline usage.
  - Multiple filter values survive pagination and ordering links.
  - Invalid filter values fail safely to server defaults.
  - Behavior is covered by unit tests.

## Phase 6 backlog integration snapshot

- [x] **Implemented**: Add workflow activity timeline contract.
- [x] **Implemented**: Add advanced list/table server query contract.
- [ ] **Open**: Add nested navigation section rendering contract.
- [x] **Completed**: Add SSR-first form error summary partial.
- [x] **Completed**: Add server-side tabs navigation template contract.
- [x] **Completed**: Add pagination page-size query helper.
- [x] **Completed**: Document feature parity matrix by maturity level.

## Phase 1 — Plan

- [x] Review backlog and identify Phase 6 selected parallel tasks.
- [x] Understand existing patterns for templates, helpers, tests.

## Phase 2 — Execute

- [x] Create timeline partial template.
- [x] Add timeline CSS to base.css.
- [x] Add timeline events to integration view context.
- [x] Include timeline in integration template.
- [x] Add `resolve_filters` / `get_filters_from_request` helpers.
- [x] Update `list_query` tag to preserve multiple filter params.
- [x] Add template contract tests for timeline.
- [x] Add unit tests for multi-filter helper and tag.

## Phase 3 — Review

- [x] Run ruff checks — pass.
- [x] Run full test suite — 50 tests pass.
- [ ] Code review and security scan.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
