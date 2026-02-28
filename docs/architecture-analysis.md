# django-material Architectural Pattern Analysis (Phase 1B)

This analysis captures core architectural patterns in `django-material` that influence migration design for `django-mui`.

## Rendering Strategy

- Primary rendering model is **server-side Django templates** with reusable template fragments.
- Client-side behavior is usually **progressive enhancement** (JS augments server-rendered markup rather than replacing it).
- UI composition is strongly tied to Django context variables and template inheritance.
- Practical implication: migration should preserve SSR-first page assembly and add React only where interaction complexity justifies hydration.

## Coupling Patterns

- **View-template coupling**: templates depend on Django view-provided context structure and naming conventions.
- **Form-template coupling**: rendering logic expects Django `Form`/`BoundField` semantics and server-side validation lifecycle.
- **Theme/layout coupling**: layout shells and component fragments are coordinated through Django template blocks and include trees.
- **URL-permission coupling**: navigation visibility and action affordances are coupled to Django URL reversing and permission checks.

## Template Overrides

- Customization typically uses Django’s template override mechanisms (`extends`, `include`, and app-level template precedence).
- Integrators often override:
  - base layout/shell templates
  - field/widget templates
  - navigation/sidebar fragments
- This creates flexibility, but also introduces implicit contracts that are easy to break during modernization.
- Compatibility priority: keep stable block names and override entry points while introducing any new React mount regions.

## Modernization Risks

| Risk | Why it matters | Mitigation direction |
| --- | --- | --- |
| Context contract drift | React/MUI layers may expect data shapes that differ from existing template context | Define explicit, versioned payload schemas for Django↔frontend bridge |
| Override breakage | Existing template overrides can fail if block names/DOM structure change | Preserve compatibility layer and document stable extension points |
| Validation mismatch | Moving form UI client-side can diverge from Django validation behavior | Keep Django as canonical validation source; enhance only presentation |
| Incremental migration complexity | Mixed template + React rendering can create duplicated concerns | Use clear island boundaries and migrate by feature slice |
| Permission drift in UI state | Client-rendered navigation/actions can expose invalid affordances | Resolve permissions server-side and pass only allowed actions to islands |

## Implication for `django-mui`

`django-mui` should adopt a hybrid approach that preserves Django-first server contracts while introducing React + MUI selectively in high-value interaction zones.
