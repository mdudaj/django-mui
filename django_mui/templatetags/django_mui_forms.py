from django import template

register = template.Library()


@register.inclusion_tag("django_mui/includes/form_field.html")
def render_form_field(field):
    if field is None:
        return {"field": None, "widget_type": "", "rendered_field": "", "help_text_id": ""}
    help_text_id = f"{field.auto_id}-helptext" if field.help_text and field.auto_id else ""
    rendered_field = (
        field.as_widget(attrs={"aria-describedby": help_text_id})
        if help_text_id
        else field.as_widget()
    )
    return {
        "field": field,
        "widget_type": field.field.widget.__class__.__name__.lower(),
        "rendered_field": rendered_field,
        "help_text_id": help_text_id,
    }
