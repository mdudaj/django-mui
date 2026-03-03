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
