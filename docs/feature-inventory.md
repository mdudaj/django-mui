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

## Inventory Baseline (Phase 1A Deliverable)

### 1) Layout System

- Current behavior: base admin-like shell template with block inheritance for page title, actions, content, and optional side regions.
- Django dependency: high (`extends` trees, block naming contracts, context-provided page metadata).
- Candidate implementation: **Hybrid** (Django controls shell/layout structure; React islands for dynamic page header actions).
- Risk: **High** (breaking block contracts can invalidate existing overrides).

### 2) Navigation

- Current behavior: sidebar/top navigation rendered from Django context; active state inferred from route/view context.
- Django dependency: high (URL reversing, permission checks, template recursion for nested menus).
- Candidate implementation: **Hybrid** (server-rendered fallback nav + hydrated MUI navigation component).
- Risk: **High** (permissions + active-state parity must be exact).

### 3) Form Rendering

- Current behavior: Django `Form`/`BoundField` rendering with template partials for labels, errors, help text, and widget wrappers.
- Django dependency: high (server-side validation lifecycle, field metadata, widget attrs).
- Candidate implementation: **Hybrid** (server-first rendering with optional React widget islands for high-interaction fields).
- Risk: **High** (client/server validation mismatch risk).

### 4) Workflow Patterns

- Current behavior: state/status surfaces and transition actions are primarily server-driven (buttons/forms bound to permissions and status).
- Django dependency: medium-high (views enforce transition rules and audit behavior).
- Candidate implementation: **React island** for state visualization + **Django endpoints** for transition execution.
- Risk: **Medium** (business-rule drift if client starts encoding transition logic).

### 5) Tables and Lists

- Current behavior: server-rendered list pages with pagination, filtering controls, and action columns.
- Django dependency: medium (queryset/view logic and context pagination objects).
- Candidate implementation: **Server template** initially, with optional React enhancement for advanced client filtering where needed.
- Risk: **Medium** (large list behavior/performance can regress if prematurely shifted client-side).

### 6) Feedback UI

- Current behavior: Django message framework for alerts and inline form errors.
- Django dependency: medium (messages injected via context/processors; rendered in shared partials).
- Candidate implementation: **Hybrid** (server-rendered alerts + optional MUI Snackbar bridge fed by serialized messages).
- Risk: **Medium** (duplicate feedback channels if both systems are not unified).

### 7) Theming

- Current behavior: theme values encoded in template/CSS assets with global style assumptions.
- Django dependency: medium (asset pipeline and template-selected classes).
- Candidate implementation: **Hybrid** (shared token layer mapped to both CSS variables and MUI theme object).
- Risk: **Medium** (visual drift during token migration).

### 8) Pro-Equivalent / Enterprise-Like Features

- Current behavior: likely includes richer dashboard widgets, enhanced table controls, or workflow conveniences in premium variants.
- Django dependency: unknown-medium (depends on implementation location: template fragments vs JS modules).
- Candidate implementation: **Phased hybrid**, prioritizing parity-critical features before adding net-new enhancements.
- Risk: **Low-Medium** (scope creep if parity and modernization are mixed in one phase).

## Recommended Prioritization

1. Preserve server-rendered layout/navigation/form contracts first.
2. Introduce React + MUI only at clearly bounded interaction hotspots.
3. Defer enterprise-like enhancements until baseline parity is validated.

## Feature parity matrix by maturity tier

This matrix tracks where `django-mui` currently stands relative to the audited
`django-material` feature areas.

| Feature area | Maturity tier | Current `django-mui` state | Backlog mapping |
| --- | --- | --- | --- |
| Layout, navigation, forms, lists, feedback, theming foundations | Implemented | Server-first contracts are available via reusable templates, helpers, and example pages in this repository. | n/a |
| Remaining full parity beyond current foundations (including deeper workflow/table/navigation enhancements) | Planned | Core contracts are in place, but parity expansion remains phased. | `docs/implementation-issues.md` issue drafts for future implementation waves |
| 1:1 cloning of proprietary/premium-only `django-material` assets | Out of scope | Project goal is OSS-compatible migration patterns, not shipping proprietary upstream assets. | n/a |
