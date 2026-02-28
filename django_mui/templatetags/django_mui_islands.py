import json

from django import template

register = template.Library()


@register.inclusion_tag("django_mui/includes/react_island.html")
def render_react_island(component, props=None, version=1):
    payload = {"version": version, "component": component, "props": props or {}}
    return {"payload_json": json.dumps(payload)}
