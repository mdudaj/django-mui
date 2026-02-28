from django import template

from django_mui.navigation import build_navigation

register = template.Library()


@register.inclusion_tag("django_mui/includes/navigation.html", takes_context=True)
def render_navigation(context, registry=None):
    request = context.get("request")
    if request is None:
        return {"navigation_items": []}
    return {"navigation_items": build_navigation(request, registry=registry)}
