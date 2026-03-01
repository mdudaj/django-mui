# django-mui Implementation Issues (Phase 3 Backlog)

Phase 2 seed backlog items are complete. The next work queue is listed below.

Use the following issue drafts to create real implementation tickets in GitHub.

## 1) Add server-rendered table/list primitives

- **Title**: `feat: add SSR-first table/list templates`
- **Scope**: Introduce reusable list/table template partials that preserve Django pagination and action patterns.
- **Acceptance criteria**:
  - Base list/table partial renders headers, rows, and empty state without JavaScript.
  - Existing Django `Paginator` objects can be passed directly from views.
  - Pattern is documented with one usage example.

## 2) Add filter/sort query contract for list pages

- **Title**: `feat: add list filtering and sorting helpers`
- **Scope**: Provide server-side helpers/template tags for preserving filter/sort query params in pagination and links.
- **Acceptance criteria**:
  - Filter and sort values survive page navigation.
  - Query contract is explicit and documented (`?q=`, `?ordering=`, `?page=` baseline).
  - Missing/invalid sort inputs fail safely to default ordering.

## 3) Add server-first feedback UI adapters

- **Title**: `feat: map django messages to mui-styled alerts`
- **Scope**: Render Django messages framework output with reusable MUI-aligned template partials.
- **Acceptance criteria**:
  - Message levels (`success`, `info`, `warning`, `error`) map to deterministic alert styles.
  - Messages render correctly with JavaScript disabled.
  - Integration guidance is added for base template usage.

## 4) Add breadcrumb contract for base shell navigation

- **Title**: `feat: add breadcrumb template contract`
- **Scope**: Extend base shell with an optional breadcrumb block/context contract that supports server-side route context.
- **Acceptance criteria**:
  - Breadcrumbs can be rendered entirely from Django context.
  - Existing `page_title`, `actions`, `navigation`, `content` blocks remain stable.
  - Active breadcrumb item is exposed with accessible markup (`aria-current="page"`).

## 5) Publish example integration app pages

- **Title**: `docs: add example pages for forms/navigation/workflow/table patterns`
- **Scope**: Add a minimal example project/pages showing recommended integration patterns for implemented features.
- **Acceptance criteria**:
  - Example pages cover base shell, forms, navigation, workflow transitions, and list/table rendering.
  - README links to example entry points.
  - Example content is intentionally minimal and server-first.

## 6) Close maturity-level documentation gaps

- **Title**: `docs: add contributor, release, and security process docs`
- **Scope**: Add missing repository docs called out in maturity planning (contributing, changelog/release flow, security reporting).
- **Acceptance criteria**:
  - `CONTRIBUTING.md` includes local QA commands and contribution workflow.
  - Release/changelog process is documented.
  - Security reporting process is documented and linked from README.
