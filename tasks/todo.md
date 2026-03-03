# Task execution board

## Active work item

* Objective: Refresh implementation backlog when no open selected tasks remain.
* Scope boundary: backlog docs and backlog contract tests only.
* Dependencies: `docs/implementation-issues.md`, `tests/test_template_contracts.py`.
* Acceptance criteria:
  - A new open backlog phase exists with non-empty selected parallel tasks.
  - Existing completed phases remain documented for implementation history.
  - Backlog documentation contract tests reflect the updated phase state.

## Phase 6 backlog integration snapshot

- [ ] **Planned**: Add workflow transition guard contract.
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

- [x] Review current backlog state and identify empty selected-task condition.
- [x] Understand existing documentation and contract test patterns.

## Phase 2 — Execute

- [x] Add a new open backlog phase with selected parallel tasks.
- [x] Keep prior completed phases untouched as history.
- [x] Update backlog contract test expectations.

## Phase 3 — Review

- [ ] Run ruff checks — pass.
- [ ] Run full test suite — pass.
- [ ] Code review and security scan.

## Validation commands

- `ruff check .`
- `ruff check . --select S`
- `python -m unittest discover -s tests -p "test_*.py"`
