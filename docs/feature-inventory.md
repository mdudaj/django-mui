# django-material Feature Inventory (Phase 1A)

This inventory captures the feature areas to audit from `django-material` so they can be mapped into `django-mui`.

## Feature Areas

| Area | What to inventory | Migration priority |
| --- | --- | --- |
| Layout system | Base templates, app shell, grid/layout utilities | High |
| Navigation | Sidebar, top nav, breadcrumbs, active-state behavior | High |
| Form rendering | Widgets, field templates, validation/error display, help text | High |
| Workflow patterns | Multi-step forms, actions, status indicators | Medium |
| Tables/lists | Data table templates, filtering/sorting patterns | Medium |
| Feedback UI | Alerts, toasts/snackbars, loading states | Medium |
| Theming | Color palettes, typography, dark/light behavior | Medium |
| Pro-equivalent features | Any enterprise-only components/extensions | Low |

## Audit Output Contract

For each feature area, capture:

1. Current `django-material` behavior
2. Dependency on Django template internals
3. Candidate `django-mui` implementation pattern (server template, React island, or hybrid)
4. Risk level for migration
