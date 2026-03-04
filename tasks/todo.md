# Task execution board

## Active work item

* Objective: Start Phase 10 backlog execution by implementing the workflow status summary contract.
* Scope boundary: minimal server-rendered workflow summary contract updates (template, view context, docs/tests).
* Dependencies: `django_mui/templates/django_mui/includes/workflow_status_summary.html`, `django_mui/templates/django_mui/examples/integration.html`, `django_mui/views.py`, `docs/implementation-issues.md`, `tests/test_template_contracts.py`, `tasks/lessons.md`.
* Acceptance criteria:
  - Workflow status summary renders from Django context with optional next-step metadata.
  - Integration example uses the new summary contract with existing workflow payloads.
  - Backlog snapshot and template contract tests reflect 15/16 completed selected items.

## Backlog integration snapshot

- **Completion (selected backlog items)**: 15/16 complete (94%); 1/16 remaining (6%).
- [x] **Implemented**: Add workflow transition guard contract.
- [x] **Implemented**: Add server-rendered table bulk-actions contract.
- [x] **Implemented**: Add navigation + breadcrumb composition contract.
- [x] **Implemented**: Add hybrid form widget islands contract.
- [x] **Implemented**: Add server+snackbar feedback bridge contract.
- [x] **Implemented**: Add navigation permission-guard contract.
- [x] **Implemented**: Add workflow timeline grouping contract.
- [x] **Implemented**: Add workflow status summary contract.
- [x] **Implemented**: Add workflow activity timeline contract.
- [x] **Implemented**: Add advanced list/table server query contract.
- [x] **Implemented**: Add nested navigation section rendering contract.
- [x] **Completed**: Add SSR-first form error summary partial.
- [x] **Completed**: Add server-side tabs navigation template contract.
- [x] **Completed**: Add pagination page-size query helper.
- [x] **Completed**: Document feature parity matrix by maturity level.

## Phase 1 — Plan

- [x] Review backlog docs and identify the next executable Phase 10 contract.
- [x] Confirm templates/views/tests to extend for workflow status summary behavior.

## Phase 2 — Execute

- [x] Add reusable `workflow_status_summary` server-rendered template partial.
- [x] Wire workflow status summary context + include into integration example.
- [x] Refresh backlog snapshot counts and focused template contract tests.

## Phase 3 — Review

- [x] Run targeted tests for changed contract areas.
- [x] Run `ruff check .`.
- [x] Run `ruff check . --select S`.
- [x] Run `python -m unittest discover -s tests -p "test_*.py"` and capture updated integration screenshot.
- [x] Run code review and codeql checker; address actionable findings.
- [x] Screenshot reference for PR: https://github.com/user-attachments/assets/85eb0bb2-abd3-4b95-8d72-54172120655e

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
