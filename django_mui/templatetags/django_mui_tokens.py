from django import template

from django_mui.design_tokens import get_css_variables, get_mui_theme_tokens

register = template.Library()


def _theme_mode(context):
    request = context.get("request")
    if request is not None:
        requested = request.GET.get("theme")
        if requested in {"light", "dark"}:
            return requested
    configured = context.get("django_mui_theme_mode")
    return configured if configured in {"light", "dark"} else "light"


@register.simple_tag(takes_context=True)
def django_mui_css_variables(context):
    mode = _theme_mode(context)
    css_variables = get_css_variables(mode)
    return "; ".join(f"{name}: {value}" for name, value in css_variables.items())


@register.simple_tag(takes_context=True)
def django_mui_theme_json(context):
    mode = _theme_mode(context)
    return get_mui_theme_tokens(mode)
