# django-mui Implementation Issues

## Porting completion snapshot

- **Selected backlog items completed**: 24/26 (92%)
- **Remaining selected backlog items**: 2/26 (8%)
- **Remaining contracts to complete**: 2 contracts in the currently selected queue.
- **Work left to finish free + pro parity scope**: 2 planned OSS parity contracts
  (workflow SLA summary + table saved-view metadata); proprietary premium-only
  1:1 cloning stays out of scope per `docs/feature-inventory.md`.

## Phase 15 Backlog (Open)

Phase 2 seed backlog items through Phase 14 backlog items are complete. Phase 15
opens the next parity-oriented implementation queue.

Use the following issue drafts to create real implementation tickets in GitHub.

### Next tasks to execute in parallel

- **Selected parallel tasks**:
  - Add server-rendered workflow SLA breach summary contract
  - Add server-rendered table saved-view metadata contract
- **Reason**: These contracts continue parity work by exposing operational workflow
  urgency and reusable list personalization metadata in SSR templates.

### 1) Add server-rendered workflow SLA breach summary contract

- **Title**: `feat: add server-rendered workflow SLA breach summary contract`
- **Scope**: Introduce a reusable workflow SLA summary partial that renders
  deterministic overdue/at-risk/on-time counts from Django context.
- **Acceptance criteria**:
  - SLA summary renders from Django context-provided metadata.
  - Existing workflow usage without SLA metadata remains backward compatible.
  - Integration example demonstrates SLA summary within existing workflow
    contracts.

### 2) Add server-rendered table saved-view metadata contract

- **Title**: `feat: add server-rendered table saved-view metadata contract`
- **Scope**: Introduce a reusable table saved-view metadata partial that renders
  active saved-view name and owner metadata from Django context.
- **Acceptance criteria**:
  - Saved-view metadata renders from Django context-provided metadata.
  - Existing table/list usage without saved-view metadata remains backward
    compatible.
  - Integration example demonstrates saved-view metadata with existing table
    contracts.

## Phase 14 Backlog (Completed)

Phase 2 seed backlog items through Phase 13 backlog items are complete. Phase 14
items are now implemented.

Use the following issue drafts to create real implementation tickets in GitHub.

### Next tasks to execute in parallel

- **Selected parallel tasks**: _None currently open in Phase 14 (all items below are implemented)._
- **Reason**: Workflow transition history and table selection summary contracts are
  implemented.

### 1) Add server-rendered workflow transition history contract

- **Title**: `feat: add server-rendered workflow transition history contract`
- **Scope**: Introduce a reusable workflow transition history partial that renders
  recent transition metadata (actor/action/timestamp) from Django context without
  JavaScript.
- **Acceptance criteria**:
  - Transition history renders from Django context-provided metadata.
  - Existing workflow usage without transition history metadata remains backward
    compatible.
  - Integration example demonstrates transition history within existing workflow
    contracts.

### 2) Add server-rendered table selection summary contract

- **Title**: `feat: add server-rendered table selection summary contract`
- **Scope**: Introduce a reusable table selection summary partial that renders
  deterministic selected-count text and clear-selection affordance from server
  context.
- **Acceptance criteria**:
  - Selection summary renders from Django context-provided metadata.
  - Existing table usage without selection summary metadata remains backward
    compatible.
  - Integration example demonstrates selection summary with existing table
    contracts.

## Phase 13 Backlog (Completed)

Phase 2 seed backlog items through Phase 12 backlog items are complete. Phase 13
items are now implemented.

Use the following issue drafts to create real implementation tickets in GitHub.

### Next tasks to execute in parallel

- **Selected parallel tasks**: _None currently open in Phase 13 (all items below are implemented)._
- **Reason**: Table toolbar actions and workflow audit banner contracts are
  implemented.

### 1) Add server-rendered table toolbar actions contract

- **Title**: `feat: add server-rendered table toolbar actions contract`
- **Scope**: Introduce a reusable table-toolbar actions partial for deterministic
  server-rendered list-level actions (export/create/help) without client
  JavaScript.
- **Acceptance criteria**:
  - Table toolbar actions render from Django context-provided metadata.
  - Existing table usage without toolbar metadata remains backward compatible.
  - Integration example demonstrates toolbar actions with existing table/list
    payloads.

### 2) Add server-rendered workflow audit banner contract

- **Title**: `feat: add server-rendered workflow audit banner contract`
- **Scope**: Introduce a reusable workflow audit banner partial for
  server-rendered provenance metadata (last actor/time/source) with deterministic
  fallback semantics.
- **Acceptance criteria**:
  - Workflow audit banner renders from Django context-provided metadata.
  - Existing workflow usage without audit metadata remains backward compatible.
  - Integration example demonstrates audit banner usage in an existing workflow
    contract.

## Phase 12 Backlog (Completed)

Phase 2 seed backlog items through Phase 11 backlog items are complete. Phase 12
items are now implemented.

Use the following issue drafts to create real implementation tickets in GitHub.

### Next tasks to execute in parallel

- **Selected parallel tasks**: _None currently open in Phase 12 (all items below are implemented)._
- **Reason**: Pagination summary and status chip primitive contracts are
  implemented.

### 1) Add server-rendered pagination summary contract

- **Title**: `feat: add server-rendered pagination summary contract`
- **Scope**: Introduce a reusable server-rendered pagination summary partial that
  exposes item ranges and total counts without relying on JavaScript state.
- **Acceptance criteria**:
  - Pagination summary renders from Django context-provided metadata.
  - Existing list/table usage without summary metadata remains backward
    compatible.
  - Integration example demonstrates pagination summary content with existing
    paginator payloads.

### 2) Add server-rendered status chip primitive contract

- **Title**: `feat: add server-rendered status chip primitive contract`
- **Scope**: Introduce a reusable status chip template primitive with
  deterministic semantic variants for shared workflow/list labels.
- **Acceptance criteria**:
  - Status chip renders from Django context-provided label and variant metadata.
  - Existing templates without chip usage remain backward
    compatible.
  - Integration example demonstrates status chip usage in at least one existing
    contract.

## Phase 11 Backlog (Completed)

Phase 2 seed backlog items through Phase 10 backlog items are complete. Phase 11
items are now implemented.

Use the following issue drafts to create real implementation tickets in GitHub.

### Next tasks to execute in parallel

- **Selected parallel tasks**: _None currently open in Phase 11 (all items below are implemented)._
- **Reason**: Table row state badges and active-filter summary contracts are
  implemented.

### 1) Add server-rendered table row state badge contract

- **Title**: `feat: add server-rendered table row state badge contract`
- **Scope**: Extend table/list rendering patterns with optional per-row state
  badges that map deterministic state names to semantic classes while preserving
  baseline row rendering.
- **Acceptance criteria**:
  - Row state badge metadata can be provided from Django context.
  - Existing row markup without badge metadata remains backward compatible.
  - Integration example demonstrates one badge-enhanced row contract.

### 2) Add server-rendered active-filter summary contract

- **Title**: `feat: add server-rendered active-filter summary contract`
- **Scope**: Introduce a reusable server-rendered summary for active list/table
  filters that can render deterministic labels and reset links without client
  JavaScript.
- **Acceptance criteria**:
  - Active filters can render from Django context-provided metadata.
  - Existing list/table usage without summary metadata remains backward
    compatible.
  - Integration example demonstrates filter summary behavior with existing query
    contracts.

## Phase 10 Backlog (Completed)

Phase 2 seed backlog items through Phase 9 backlog items are complete. Phase 10
items are now implemented.

Use the following issue drafts to create real implementation tickets in GitHub.

### Next tasks to execute in parallel

- **Selected parallel tasks**: _None currently open in Phase 10 (all items below are implemented)._
- **Reason**: Workflow status summary and table column metadata contracts are
  implemented.

### 1) Add workflow status summary contract

- **Title**: `feat: add workflow status summary contract`
- **Scope**: Introduce a reusable server-rendered status summary partial for
  workflow detail views with deterministic semantics for current state and
  optional next actions.
- **Acceptance criteria**:
  - Status summary renders entirely from Django context without JavaScript.
  - Optional next-step metadata can be displayed without coupling to transition
    execution logic.
  - Integration example demonstrates status summary usage with existing workflow
    context payloads.

### 2) Add server-rendered table column metadata contract

- **Title**: `feat: add server-rendered table column metadata contract`
- **Scope**: Extend table rendering contracts to support optional column
  metadata (alignment, emphasis, and semantic labels) while preserving baseline
  header/row behavior.
- **Acceptance criteria**:
  - Table columns can declare optional metadata from Django context.
  - Existing list/table usage without metadata remains backward compatible.
  - Integration example demonstrates one metadata-enhanced table contract.

## Phase 9 Backlog (Completed)

Phase 2 seed backlog items through Phase 8 backlog items are complete. Phase 9
opens the next implementation queue for parity-oriented expansion.

Use the following issue drafts to create real implementation tickets in GitHub.

### Next tasks to execute in parallel

- **Selected parallel tasks**: _None currently open in Phase 9 (all items below are implemented)._
- **Reason**: These contracts extend mature server-first foundations with
  bounded hybrid interactivity aligned to documented parity priorities.

### 1) Add hybrid form widget islands contract

- **Title**: `feat: add hybrid form widget islands contract`
- **Scope**: Introduce a server-first contract for optional React island widget
  enhancement on high-interaction form fields without breaking non-JS fallback.
- **Acceptance criteria**:
  - Form fields can declare optional island metadata from Django context.
  - Baseline server-rendered field markup remains the default fallback.
  - Integration example demonstrates one high-interaction field using the
    existing island bootstrapping contract.

### 2) Add server+snackbar feedback bridge contract

- **Title**: `feat: add server+snackbar feedback bridge contract`
- **Scope**: Extend feedback UI contracts with an optional bridge that maps
  Django messages to a deterministic serialized payload for snackbar islands.
- **Acceptance criteria**:
  - Existing server-rendered alerts remain backward compatible.
  - Message payload can be serialized for optional client snackbar consumption.
  - Integration example demonstrates both server fallback and optional payload.

## Phase 8 Backlog (Completed)

Phase 2 seed backlog items through Phase 7 backlog items are complete. Phase 8
items are now implemented.

Use the following issue drafts to create real implementation tickets in GitHub.

### Next tasks to execute in parallel

- **Selected parallel tasks**: _None currently open in Phase 8 (all items below are implemented)._
- **Reason**: These contracts extend current workflow and table foundations with
  high-value server-first capabilities and minimal coupling.

### 1) Add navigation permission-guard contract

- **Title**: `feat: add navigation permission-guard contract`
- **Scope**: Add a reusable server-side contract for hiding/marking unavailable
  navigation items when user permissions are insufficient.
- **Acceptance criteria**:
  - Navigation items can be flagged unavailable from Django context.
  - Unavailable entries render deterministic fallback semantics.
  - Integration example demonstrates mixed available/unavailable entries.

### 2) Add workflow timeline grouping contract

- **Title**: `feat: add workflow timeline grouping contract`
- **Scope**: Extend timeline patterns with optional grouping labels and explicit
  empty-state behavior for server-rendered workflows.
- **Acceptance criteria**:
  - Timeline can render grouped entries from Django context without JavaScript.
  - Empty timeline payloads render a deterministic fallback message.
  - Integration example demonstrates grouped and empty-state timeline payloads.

## Phase 7 Backlog (Completed)

Phase 2 seed backlog items through Phase 6 backlog items are complete. Phase 7
items are now implemented.

Use the following issue drafts to create real implementation tickets in GitHub.

### Next tasks to execute in parallel

- **Selected parallel tasks**: _None currently open in Phase 7 (all items below are implemented)._
- **Reason**: Workflow transition guards, table bulk actions, and navigation +
  breadcrumb composition contracts are implemented.

### 1) Add workflow transition guard contract

- **Title**: `feat: add workflow transition guard contract`
- **Scope**: Add a reusable server-side contract for disabled/blocked workflow
  transitions with deterministic reason messaging.
- **Acceptance criteria**:
  - Transition actions can be marked disabled from Django context.
  - Disabled transitions render a deterministic reason for users.
  - Integration example demonstrates enabled and blocked transitions.

### 2) Add server-rendered table bulk-actions contract

- **Title**: `feat: add server-rendered table bulk-actions contract`
- **Scope**: Extend the list/table integration with an optional bulk-action form
  contract that works without JavaScript.
- **Acceptance criteria**:
  - Rows expose selectable state in server-rendered markup.
  - Bulk action submission can be posted with selected IDs.
  - Empty/invalid submissions fail safely with user feedback.

### 3) Add navigation + breadcrumb composition contract

- **Title**: `feat: add composed navigation and breadcrumb contract`
- **Scope**: Define a server-rendered composition pattern where navigation
  sections and breadcrumbs share current-route context.
- **Acceptance criteria**:
  - Breadcrumb current item stays aligned with active navigation state.
  - Base template block contracts remain backward compatible.
  - Accessibility semantics (`aria-current`) remain explicit in both patterns.

## Phase 6 Backlog (Completed)

Phase 2 seed backlog items through Phase 5 backlog items are complete. Phase 6
continues the implementation queue with new parity-focused tasks. All Phase 6
items are now implemented.

Use the following issue drafts to create real implementation tickets in GitHub.

### Next tasks to execute in parallel

- **Selected parallel tasks**: _None currently open in Phase 6 (all items below are implemented)._
- **Reason**: Workflow timeline, advanced list/table query, and nested navigation section contracts are implemented.

### 1) Add workflow activity timeline contract

- **Title**: `feat: add server-first workflow activity timeline`
- **Scope**: Add a reusable server-rendered timeline partial for workflow events and expose an integration example context contract.
- **Acceptance criteria**:
  - Timeline renders event entries from Django context without JavaScript.
  - Event entries support semantic timestamps and status labels.
  - Integration example demonstrates timeline usage with existing workflow payload patterns.

### 2) Add advanced list/table server query contract

- **Title**: `feat: extend list query helpers for multi-filter contracts`
- **Scope**: Expand list query helpers and table integration patterns to preserve multiple filter parameters alongside ordering, pagination, and page size.
- **Acceptance criteria**:
  - Multiple filter values survive pagination and ordering links.
  - Invalid filter values fail safely to server defaults.
  - Behavior is covered by unit tests for helper/tag contracts.

### 3) Add nested navigation section rendering contract

- **Title**: `feat: add nested navigation section partial`
- **Scope**: Introduce a server-rendered navigation section partial for grouped links with active-state support for nested items.
- **Acceptance criteria**:
  - Navigation sections render from Django context-provided groups/items.
  - Active-state behavior remains compatible with current view-name and path-prefix matching.
  - Markup includes accessible group labels and current-page semantics.

## Phase 5 Backlog (Completed)

Phase 2 seed backlog items, Phase 3 backlog items, Phase 4 backlog items, and
Phase 5 backlog items are complete.

Use the following issue drafts to create real implementation tickets in GitHub.

### Next tasks to execute in parallel

- **Selected parallel tasks**: _None currently open in Phase 5 (all items below are implemented)._
- **Reason**: Form error summary, tabs contract, page-size query behavior, and parity matrix documentation are implemented.

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
