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
