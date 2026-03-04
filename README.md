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

`django-mui` is currently server-first and does not require local MUI `node_modules`
for baseline example styling. Shared styles are shipped as static assets in
`django_mui/static/django_mui/`.

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

## Server-first messages adapter

The base template includes `django_mui/includes/messages.html` and maps Django message levels to deterministic alert classes:

- `success` -> `mui-alert-success`
- `info` (default) -> `mui-alert-info`
- `warning` -> `mui-alert-warning`
- `error` -> `mui-alert-error`

When `snackbar_messages_payload` is provided in template context, messages are also
serialized via `json_script` (`id="django-mui-snackbar-messages"`) for optional
snackbar island consumption while preserving server-rendered alert fallback.

## Breadcrumb context contract

The base template includes `django_mui/includes/breadcrumbs.html` and renders breadcrumbs from a `breadcrumbs` context variable:

```python
breadcrumbs = [
    {"label": "Orders", "url": "/orders/"},
    {"label": "Order #123", "active": True},
]
```

The active/last breadcrumb item is rendered with `aria-current="page"`.

## Server-rendered table/list primitive

`django_mui/includes/table.html` renders headers, rows, empty state, and optional pagination from a Django `page_obj`.

```django
{% include "django_mui/includes/table.html" with columns=columns rows=rows page_obj=page_obj %}
```

Example view shape:

```python
allowed_orderings = ["order", "-order"]
ordering = get_ordering_from_request(request, allowed_orderings, "order")
allowed_page_sizes = [10, 25, 50]
page_size = get_page_size_from_request(request, allowed_page_sizes, 25)
paginator = Paginator(order_rows, per_page=page_size)
page_obj = paginator.get_page(request.GET.get("page"))
columns = ["Order", "Customer", "Status"]
rows = [[row.number, row.customer_name, row.status] for row in page_obj.object_list]
```

List pages use an explicit query contract for server-rendered filtering/sorting:

- `?q=` search term
- `?ordering=` sort key
- `?page_size=` validated page size
- `?page=` paginator page

Pagination links from `django_mui/includes/table.html` preserve `q`, `ordering`, and
valid `page_size` values.
Use `django_mui.list_query.get_ordering_from_request(request, allowed_orderings, default_ordering)`
and `django_mui.list_query.get_page_size_from_request(request, allowed_page_sizes, default_page_size)`
to safely fall back when missing/invalid values are provided.

## Example integration pages

Include `django_mui.urls` in your project URLconf to access server-first example pages:

- `django_mui_example_index` (`examples/`)
- `django_mui_example_integration` (`examples/integration/`)

## Form field adapter

`django_mui` includes a server-first form field adapter tag that renders labels, errors, help text, and required state while preserving Django form POST behavior.

```django
{% load django_mui_forms %}
{% render_form_field form.email %}
```

High-interaction fields can opt into an island payload without breaking baseline
SSR rendering:

```django
{% render_form_field form.q island=q_field_island %}
```

For top-of-form validation summaries, include the reusable server-rendered partial:

```django
{% include "django_mui/includes/form_error_summary.html" with form=form %}
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

Additional maturity-level process docs:

- Contributing guide: `CONTRIBUTING.md`
- Release/changelog process: `docs/release-process.md`
- Security reporting process: `SECURITY.md`

## Implementation issue backlog

The currently selected implementation backlog queue is complete; implementation
history and future issue-draft planning are captured in
`docs/implementation-issues.md`.

Feature parity maturity tracking is documented in the `Feature parity matrix by maturity tier` section of `docs/feature-inventory.md`.

## Agentic workflow (ported)

Workflow assets are now available in-repo:

- `CLAUDE.md`
- `COPILOT.md`
- `tasks/todo.md`
- `tasks/lessons.md`
- `.github/ISSUE_TEMPLATE/delivery-work-item.md`
- `.github/pull_request_template.md`

Helper scripts:

```bash
# fast local loop
.github/scripts/local_fast_feedback.sh

# run full merge-gate baseline
.github/scripts/local_fast_feedback.sh --full-gate

# scaffold workflow files into another repo
.github/scripts/scaffold_agentic_workflow.sh --dry-run /path/to/repo
```

## Parity status with django-material

Completing the current implementation backlog does **not** mean all `django-material` free/pro features are fully ported to `django-mui`.
The current scope delivers baseline migration foundations; full feature parity remains a phased effort guided by `docs/feature-inventory.md`.
