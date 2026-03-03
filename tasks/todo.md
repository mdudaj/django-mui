# Task execution board

## Active work item

* Objective: Implement Phase 6 remaining task (nested navigation section).
* Scope boundary: nav section partial, CSS, integration example, tests.
* Dependencies: `django_mui/templates/django_mui/includes/nav_section.html`, CSS, views.
* Acceptance criteria:
  - Navigation sections render from Django context-provided groups/items.
  - Active-state includes `aria-current="page"` semantics.
  - Markup includes accessible group labels.
  - Integration example demonstrates nav section usage.
  - Behavior is covered by template contract tests.

## Phase 6 backlog integration snapshot

- [x] **Implemented**: Add workflow activity timeline contract.
- [x] **Implemented**: Add advanced list/table server query contract.
- [x] **Implemented**: Add nested navigation section rendering contract.
- [x] **Completed**: Add SSR-first form error summary partial.
- [x] **Completed**: Add server-side tabs navigation template contract.
- [x] **Completed**: Add pagination page-size query helper.
- [x] **Completed**: Document feature parity matrix by maturity level.

## Phase 1 — Plan

- [x] Review backlog and identify remaining Phase 6 task.
- [x] Understand existing patterns for templates, helpers, tests.

## Phase 2 — Execute

- [x] Create nav section partial template.
- [x] Add nav section CSS to base.css.
- [x] Add nav_sections to integration view context.
- [x] Include nav section in integration template.
- [x] Add template contract tests for nav section.
- [x] Update backlog to mark Phase 6 complete.

## Phase 3 — Review

- [x] Run ruff checks — pass.
- [x] Run full test suite — pass.
- [x] Code review and security scan.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
