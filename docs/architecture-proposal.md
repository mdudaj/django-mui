# django-mui Architecture Proposal (Phase 1C)

This proposal defines a minimal hybrid architecture to modernize `django-material` patterns with React + MUI while keeping Django-first ergonomics.

## Core Architecture

1. **Django remains system-of-record** for routing, permissions, forms, and server validation.
2. **React + MUI render interactive components** in targeted islands mounted from Django templates.
3. **Progressive enhancement default**: pages work without JavaScript for baseline flows.

## Django ↔ React Bridge

- Server template emits a mount node and JSON payload:
  - `component`: registered component name
  - `props`: serialized server data
- Frontend bootstrap mounts the matching React component from a registry.
- Keep payload schema explicit and versioned to avoid template/frontend drift.

Example payload contract:

```json
{
  "version": 1,
  "component": "WorkflowStatusCard",
  "props": {
    "object_id": 42,
    "state": "pending_review",
    "allowed_transitions": ["approve", "reject"]
  }
}
```

## Navigation Model

- Define a Django-side navigation registry (label, route, icon, permissions).
- Render static fallback navigation in templates.
- Hydrate enhanced MUI navigation for responsive behavior and richer state.

Registry shape (Python-side):

`{id, label, route_name, icon, required_permissions, children}`

## Form Strategy

- Keep Django forms as the canonical definition and validation source.
- Start with server-rendered form templates styled to match MUI tokens.
- Introduce React field components only for high-interaction widgets (date/time pickers, async selects).
- Use one field adapter contract for React-enhanced widgets:
  - input: `{name, value, errors, help_text, required, widget_type}`
  - output: standard Django POST fields (no alternate submit format)

## Workflow Adapter Model

- Represent workflows as Django-side state machines (or explicit status fields).
- Expose current state + allowed transitions to React components through serialized props.
- Execute transitions through Django endpoints to preserve permission and audit logic.
- Transition endpoint contract:
  - request: `{transition, object_id, csrfmiddlewaretoken}`
  - response: `{ok, state, allowed_transitions, messages}`

## Migration Plan

1. Build shared design tokens + base template shell.
2. Port navigation and layout first.
3. Port form rendering patterns.
4. Add workflow-oriented React islands only where interaction benefits are clear.
