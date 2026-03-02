# Task execution board

## Active work item

* Objective: Ensure example pages include visible baseline styling without local MUI `node_modules`.
* Scope boundary: minimal template/static contract update and focused tests for style asset loading.
* Dependencies: `django_mui/templates/django_mui/base.html`, `django_mui/static/django_mui/`, `tests/test_template_contracts.py`.
* Acceptance criteria:
  - base template loads a stylesheet for shared UI primitives,
  - README clarifies why `node_modules` is not required,
  - tests enforce the style asset contract.

## Phase 5 backlog integration snapshot

- [x] **Open**: Add baseline example stylesheet contract (issue: missing visible styles in screenshots).
- [x] **Completed**: Add SSR-first form error summary partial.
- [x] **Completed**: Add server-side tabs navigation template contract.
- [x] **Completed**: Add pagination page-size query helper.

## Phase 1 — Plan

- [x] Confirm impacted templates/docs and style loading path.
- [x] Define minimal stylesheet contract and selector scope.
- [x] Identify README references to update.

## Phase 2 — Execute

- [x] Add shared stylesheet and include it from base template.
- [x] Add/update focused tests for stylesheet contract.
- [x] Document no-node_modules styling approach in README.

## Phase 3 — Review

- [x] Run targeted checks and record results.
- [x] Run merge-gate checks and record results.
- [x] Capture UI screenshot showing applied styles.
- [ ] Document risk review and final outcome.
- [ ] Add lessons to `tasks/lessons.md`.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
