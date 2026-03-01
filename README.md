# django-mui

Repository bootstrap and Phase 1 planning artifacts for migrating `django-material` patterns toward a Django + React + MUI hybrid approach.

## Implementation bootstrap

Initial package scaffold has been added under `django_mui/`.

```python
INSTALLED_APPS = [
    # ...
    "django_mui",
]
```

## Base template shell

`django_mui/templates/django_mui/base.html` provides stable server-rendered blocks:

- `page_title`
- `actions`
- `navigation`
- `content`

Override example:

```django
{% extends "django_mui/base.html" %}

{% block page_title %}Orders{% endblock %}

{% block navigation %}
  <a href="{% url 'orders:list' %}">Orders</a>
{% endblock %}

{% block content %}
  <p>Rendered without JavaScript.</p>
{% endblock %}
```

Default navigation can be defined server-side with a registry in settings:

```python
DJANGO_MUI_NAVIGATION = [
    {
        "id": "orders",
        "label": "Orders",
        "route_name": "orders:list",
        "icon": "list_alt",
        "required_permissions": ["orders.view_order"],
        "children": [],
    }
]
```

`django_mui` filters this registry by `required_permissions` and marks active items from the current request route.

## Form field adapter

`django_mui` includes a server-first form field adapter tag that renders labels, errors, help text, and required state while preserving Django form POST behavior.

```django
{% load django_mui_forms %}
{% render_form_field form.email %}
```

## React island mount contract

`django_mui` provides a server-emitted payload contract for progressive React islands.

```django
{% load django_mui_islands %}
{% render_react_island "WorkflowStatusCard" props=workflow_payload %}
```

Payload shape:

- `version`
- `component`
- `props`

## Workflow transition endpoint contract

`django_mui.urls` includes a transition endpoint at `workflow/transition/` named `django_mui_workflow_transition`.

Configure a server-side handler to enforce permissions and transition rules:

```python
DJANGO_MUI_WORKFLOW_TRANSITION_HANDLER = "myapp.workflows.transition_handler"
```

Handler signature:

- input: `request`, `transition`, `object_id`
- output: `{ok, state, allowed_transitions, messages}`

Demo island integration:

```django
{% load django_mui_islands %}
{% render_react_island "WorkflowStatusCard" props=workflow_payload %}
```

## Shared design tokens

`django_mui.design_tokens.TOKEN_SOURCE` is the single source of truth for base color tokens.

- Django template layer consumes these as CSS variables on `:root`.
- MUI layer consumes the same source via JSON emitted in
  `#django-mui-theme-tokens`.

Light/dark mode hook:

- Append `?theme=light` or `?theme=dark` to pages that use the base template.

Visual parity check page:

- `django_mui_design_token_parity` (`design-tokens/parity/`)

## Phase 1 deliverables

- Feature inventory: `docs/feature-inventory.md`
- Architectural pattern analysis: `docs/architecture-analysis.md`
- Architecture proposal: `docs/architecture-proposal.md`
- OSS maturity model: `docs/OSS_MATURITY_MODEL.md`
- QA evaluation contract: `docs/QA_EVALUATION_SPEC.md`

## Documentation status

Phase 1 documentation deliverables are complete.

Remaining documentation work is tied to later maturity levels (for example: contributor guidelines/code of conduct, release/changelog process, public examples, and security reporting process).

## Implementation issue backlog

Issue drafts for real implementation work are captured in `docs/implementation-issues.md`.

## Parity status with django-material

Completing the current implementation backlog does **not** mean all `django-material` free/pro features are fully ported to `django-mui`.
The current scope delivers baseline migration foundations; full feature parity remains a phased effort guided by `docs/feature-inventory.md`.
