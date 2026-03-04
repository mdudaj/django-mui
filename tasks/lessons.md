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

* Date: 2026-03-03
* Failure signature: Navigation and breadcrumb labels drifted because each section hard-coded current-page copy separately.
* Root cause: Integration context duplicated current-route metadata in two places instead of deriving both from one source.
* Preventive rule: For composed route-context contracts, define one shared context object and reuse it across navigation and breadcrumb payloads.
* Verification added: `tests.test_template_contracts` assertions for shared `current_nav_item` and aligned breadcrumb/nav context values.

* Date: 2026-03-03
* Failure signature: Backlog continuation stalled because Phase 7 remained marked open after all listed items were implemented.
* Root cause: Phase status text and selected-task metadata were not advanced when the final Phase 7 item was finished.
* Preventive rule: When the last selected task in an open phase is completed, immediately mark that phase completed and open the next phase in the same update.
* Verification added: `test_implementation_backlog_tracks_open_and_completed_phases` now asserts `Phase 8 Backlog (Open)` and `Phase 7 Backlog (Completed)`.

* Date: 2026-03-03
* Failure signature: Timeline contract test failed after introducing grouped + empty-state branches.
* Root cause: Test assertion still expected `{% if timeline_events %}` while template switched to `{% elif timeline_events %}` to preserve grouped-priority flow.
* Preventive rule: When control-flow blocks change (`if`/`elif`), update literal template-contract assertions in the same patch.
* Verification added: `tests.test_template_contracts.TemplateContractTests.test_timeline_partial_renders_events_with_status_and_timestamp`.

* Date: 2026-03-04
* Failure signature: Permission-guard nav item rendered fallback reason text but lacked explicit accessible linkage between disabled label and reason.
* Root cause: Initial unavailable-item markup added `aria-disabled` only, without deterministic `aria-describedby` target ID.
* Preventive rule: For every disabled/unavailable UI affordance, include stable ID + `aria-describedby` wiring to its reason text.
* Verification added: `test_nav_section_partial_renders_groups_with_accessible_labels` plus rendered fallback test `test_nav_section_partial_renders_default_unavailable_reason`.

* Date: 2026-03-04
* Failure signature: Backlog continuation became ambiguous because docs still showed Phase 8 as open after both selected tasks were already implemented.
* Root cause: Phase status text in `docs/implementation-issues.md` was not advanced to the next phase when the active queue was completed.
* Preventive rule: When all selected tasks in the open phase are implemented, mark that phase completed and open the next phase in the same backlog update.
* Verification added: `test_implementation_backlog_tracks_open_and_completed_phases` now asserts `Phase 9 Backlog (Open)` and `Phase 8 Backlog (Completed)`.

* Date: 2026-03-04
* Failure signature: Porting status required manual interpretation because completion percentage was not explicitly stated in backlog docs.
* Root cause: `docs/implementation-issues.md` listed open/completed phases but omitted a concise numeric snapshot of selected-task completion.
* Preventive rule: Keep a deterministic completion snapshot (`completed/total` and `remaining/total`) at the top of active implementation backlog docs.
* Verification added: `test_implementation_backlog_tracks_open_and_completed_phases` now asserts the snapshot heading and percentage text.

* Date: 2026-03-04
* Failure signature: Optional form island metadata could raise `AttributeError` when a non-dict value was passed into `render_form_field`.
* Root cause: The initial contract assumed `island` always had `.get(...)` available and skipped runtime type guarding.
* Preventive rule: For optional template-tag metadata contracts, always validate input shape (`isinstance(..., dict)`) before nested lookup.
* Verification added: `test_form_field_tag_accepts_optional_island_metadata` now asserts guarded island access patterns in `django_mui_forms.py`.

* Date: 2026-03-04
* Failure signature: Backlog continuation request was ambiguous because docs showed all selected items complete with no open next phase.
* Root cause: `docs/implementation-issues.md` was left at a fully completed queue without promoting a new actionable phase.
* Preventive rule: When a phase reaches 100% selected completion, open the next phase in the same update and refresh snapshot totals + contract tests together.
* Verification added: `test_implementation_backlog_tracks_open_and_completed_phases` now asserts `Phase 10 Backlog (Open)` and updated 14/16, 2/16 snapshot text.

* Date: 2026-03-04
* Failure signature: Workflow status summary partial raised `VariableDoesNotExist` when rendering `current_state` fallback in templates that only passed `current_state_label`.
* Root cause: Chained `default` filters forced evaluation of a missing nested key before fallback could resolve.
* Preventive rule: For optional nested template keys, prefer explicit `{% if %}/{% elif %}` checks over chained `default` filters.
* Verification added: `test_workflow_status_summary_partial_supports_optional_next_steps` now asserts explicit current-state fallback branches.

* Date: 2026-03-04
* Failure signature: Table column metadata contract required indexed access to `columns` inside template loops without native list indexing support.
* Root cause: Django templates do not support direct dynamic list indexing for parallel column/cell metadata lookup.
* Preventive rule: When template contracts need index-based access, add a narrow, validated template filter and cover invalid-index behavior with unit tests.
* Verification added: `tests/test_list_query.py` now covers `list_index` valid/invalid inputs and `tests/test_template_contracts.py` asserts metadata indexing usage in `table.html`.
