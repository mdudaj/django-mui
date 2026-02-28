# django-mui Implementation Issues (Phase 2 Seed Backlog)

Use the following issue drafts to create real implementation tickets in GitHub.

## 1) Bootstrap Django app package for `django-mui`

- **Title**: `feat: bootstrap django-mui package skeleton`
- **Scope**: Create initial Python package structure, app config, and installation path for reuse in Django projects.
- **Acceptance criteria**:
  - Package layout exists under `django_mui/`.
  - Django app can be added to `INSTALLED_APPS` without errors.
  - Basic README usage snippet references package install + setup.

## 2) Implement base template shell + stable block contracts

- **Title**: `feat: add SSR-first base shell templates`
- **Scope**: Add base layout templates that preserve override points needed for migration compatibility.
- **Acceptance criteria**:
  - Base template defines stable blocks for page title, actions, navigation, and content.
  - Template override example is documented.
  - Rendering works without JavaScript.

## 3) Add navigation registry with permission-aware rendering

- **Title**: `feat: implement django-side navigation registry`
- **Scope**: Introduce Python-side nav schema and server-rendered fallback menu.
- **Acceptance criteria**:
  - Registry shape follows `{id, label, route_name, icon, required_permissions, children}`.
  - Navigation renders active state based on request route.
  - Unauthorized items are excluded server-side.

## 4) Deliver server-first form rendering adapters

- **Title**: `feat: add form field template adapters for mui styling`
- **Scope**: Build template adapters that map Django `BoundField` data to MUI-aligned markup.
- **Acceptance criteria**:
  - Labels, errors, help text, and required state are rendered consistently.
  - Server-side validation remains canonical.
  - Existing Django POST handling is unchanged.

## 5) Create Django↔React island bootstrap and registry

- **Title**: `feat: add react island mount contract`
- **Scope**: Implement a frontend bootstrap that hydrates registered components using server-emitted JSON payloads.
- **Acceptance criteria**:
  - Payload contract supports `version`, `component`, and `props`.
  - Unknown component names fail safely.
  - Pages still function when JS is unavailable.

## 6) Add workflow transition endpoint contract + demo island

- **Title**: `feat: implement workflow transition API contract`
- **Scope**: Add transition endpoint shape and one sample workflow status component integration.
- **Acceptance criteria**:
  - Endpoint accepts `{transition, object_id, csrfmiddlewaretoken}`.
  - Response returns `{ok, state, allowed_transitions, messages}`.
  - Permissions and transition rules are enforced server-side.

## 7) Define shared design token layer

- **Title**: `feat: introduce shared design tokens for django + mui`
- **Scope**: Create an initial token system that can drive both template CSS variables and MUI theme values.
- **Acceptance criteria**:
  - Token source is defined once and consumed in both layers.
  - Light/dark mode hooks are documented.
  - Basic visual parity check page exists.

## 8) Setup real CI checks for implementation phase

- **Title**: `chore: replace placeholder QA workflow with real checks`
- **Scope**: Upgrade CI from placeholder echo to lint/test/security checks once implementation code is added.
- **Acceptance criteria**:
  - CI runs unit tests and fails on regressions.
  - CI runs formatting/lint checks.
  - CI publishes clear failure logs for contributors.
