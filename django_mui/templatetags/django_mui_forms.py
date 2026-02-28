from django import template

register = template.Library()


@register.inclusion_tag("django_mui/includes/form_field.html")
def render_form_field(field):
    if field is None:
        return {"field": None, "widget_type": ""}
    return {
        "field": field,
        "widget_type": field.field.widget.__class__.__name__.lower(),
    }
