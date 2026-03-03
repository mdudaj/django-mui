# Lessons learned

Use this file to prevent repeated mistakes across sessions.

## Entry template

* Date:
* Failure signature:
* Root cause:
* Preventive rule:
* Verification added:

---

* Date: 2026-03-02
* Failure signature: Integration screenshot showed mostly unstyled default HTML, causing confusion about missing MUI library modules.
* Root cause: Base template shipped design tokens and JS islands but no shared stylesheet to style existing `.mui-*` server-rendered classes.
* Preventive rule: Keep a baseline stylesheet linked from `django_mui/base.html` whenever new shared utility classes are introduced.
* Verification added: Template contract test now asserts `django_mui/base.css` is linked and stylesheet includes `.mui-alert` classes.

* Date: 2026-03-02
* Failure signature: Backlog state update to "Phase 5 Backlog (Completed)" broke a contract test expecting "Phase 5 Backlog (Open)".
* Root cause: Documentation contract tests hard-coded the previous backlog state and were not updated alongside the backlog progression change.
* Preventive rule: Whenever backlog phase status text changes, update contract tests in the same patch.
* Verification added: `test_implementation_backlog_tracks_open_and_completed_phases` now asserts the completed Phase 5 heading and completion text.

* Date: 2026-03-02
* Failure signature: Continuing backlog planning from a completed phase left the active queue empty and blocked next implementation selection.
* Root cause: `docs/implementation-issues.md` had no open phase after Phase 5 completion, so "selected parallel tasks" stayed at none.
* Preventive rule: When a phase is marked completed, immediately open the next phase with at least two concrete selected tasks.
* Verification added: `test_implementation_backlog_tracks_open_and_completed_phases` now asserts `Phase 6 Backlog (Open)` and its new task headings.

* Date: 2026-03-03
* Failure signature: N/A (clean implementation).
* Root cause: Phase 6 selected parallel tasks (timeline + multi-filter) implemented smoothly using established patterns.
* Preventive rule: When adding new template partials, always add matching CSS classes, integration example context, and template contract tests in the same patch.
* Verification added: 13 new tests covering timeline partial contract, multi-filter helpers, and template tag behavior.

* Date: 2026-03-03
* Failure signature: Backlog queue became non-actionable because the active phase had no selected parallel tasks.
* Root cause: Phase completion updates documented "none open" but did not immediately create a follow-on open phase with concrete tasks.
* Preventive rule: Whenever a phase is marked completed, open the next phase in the same update and select at least two executable tasks.
* Verification added: `test_implementation_backlog_tracks_open_and_completed_phases` now asserts the new `Phase 7 Backlog (Open)` task headings.

* Date: 2026-03-03
* Failure signature: Disabled workflow transitions risked weak accessibility semantics because the reason text was not programmatically tied to the disabled control.
* Root cause: Initial contract rendered disabled reason text visually, but did not provide a relationship attribute from button to reason element.
* Preventive rule: For every disabled action contract, wire reason text with deterministic IDs and `aria-describedby` from the control.
* Verification added: Template contract test now asserts `aria-describedby` and `mui-workflow-transition-reason-` marker usage in `workflow_transitions.html`.

* Date: 2026-03-03
* Failure signature: Integration page failed with `VariableDoesNotExist` when rendering bulk-selection fallback IDs.
* Root cause: Django template `default` filter evaluated the fallback expression (`row.0`) even when `row.id` existed on dict rows.
* Preventive rule: Avoid fallback expressions that perform unsafe lookups in template filters; prefer deterministic values like `forloop.counter0`.
* Verification added: Manual render check of `/examples/integration/` plus `tests.test_template_contracts` coverage for `row.id|default:forloop.counter0`.
