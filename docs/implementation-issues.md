# django-mui Implementation Issues

## Phase 5 Backlog (Open)

All prior backlog items are complete.

Use the following issue drafts to create real implementation tickets in GitHub.

### Next tasks to execute in parallel

- **Selected parallel tasks**:
  1. Document feature parity matrix by maturity level.
- **Reason**: Form error summary partial, tabs contract, and page-size query behavior are implemented; parity matrix documentation is the next independent backlog task.

### 1) Add SSR-first form error summary partial

- **Title**: `feat: add reusable form error summary partial`
- **Scope**: Introduce a template partial that renders form-wide and field-level validation errors in an accessible summary at the top of forms.
- **Acceptance criteria**:
  - Partial renders non-field and field errors without JavaScript.
  - Summary includes accessible heading/landmark semantics.
  - Pattern is documented with one integration example.

### 2) Add server-side tabs navigation template contract

- **Title**: `feat: add server-rendered tabs partial`
- **Scope**: Provide a reusable tabs partial for section-level navigation driven fully by Django context.
- **Acceptance criteria**:
  - Tabs can be rendered from context-provided items (`label`, `url`, `is_active`).
  - Active tab includes accessible state (`aria-current="page"` or equivalent).
  - Partial degrades gracefully with JavaScript disabled.

### 3) Add pagination page-size query helper

- **Title**: `feat: add page-size query contract helper`
- **Scope**: Extend list query helpers to preserve and validate optional page-size parameters.
- **Acceptance criteria**:
  - `page_size` value survives pagination links.
  - Invalid/unbounded values fail safely to defaults.
  - Behavior is covered by unit tests.

### 4) Document feature parity matrix by maturity level

- **Title**: `docs: add feature parity matrix with maturity tiers`
- **Scope**: Expand the feature inventory with explicit parity tiers (`implemented`, `planned`, `out of scope`) to guide roadmap decisions.
- **Acceptance criteria**:
  - Matrix references existing implemented building blocks.
  - Planned gaps map to backlog issue drafts.
  - README links to the updated matrix section.

## Phase 4 Backlog (Completed)

Phase 2 seed backlog items, Phase 3 backlog items, and Phase 4 backlog items are complete.

Use the following issue drafts to create real implementation tickets in GitHub.

### Next tasks to execute in parallel

- **Selected parallel tasks**: _None currently open in Phase 4 (all items below are implemented)._
- **Reason**: Both navigation active-state improvements are implemented and covered by unit tests.

### 1) Improve navigation active-state matching for nested routes

- **Title**: `feat: support active-state matching by route prefix`
- **Scope**: Allow navigation items to stay active for nested/detail routes by matching optional route prefix metadata in addition to exact view-name checks.
- **Acceptance criteria**:
  - Navigation items can declare route prefixes for active-state matching.
  - Existing exact `view_name` matching remains backward compatible.
  - Behavior is covered by unit tests in `tests/test_navigation.py`.

### 2) Improve navigation active-state matching for URL path prefixes

- **Title**: `feat: support active-state matching by URL path prefix`
- **Scope**: Allow navigation items to stay active for nested/detail routes by matching optional request-path prefixes when view-name context is absent.
- **Acceptance criteria**:
  - Navigation items can declare URL path prefixes for active-state matching.
  - Existing exact `view_name` and route-prefix matching remain backward compatible.
  - Behavior is covered by unit tests in `tests/test_navigation.py`.

## Phase 3 Backlog (Completed)

Phase 2 seed backlog items are complete. Phase 3 backlog items are also complete and tracked below for implementation-history reference.

Use the following issue drafts to create real implementation tickets in GitHub.

## Next tasks to execute in parallel

- **Selected parallel tasks**: _None currently open in Phase 3 (all items below are implemented)._ 
- **Reason**: Phase 3 work queue is complete; remaining feature-parity planning continues in the feature inventory and future implementation phases.

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
