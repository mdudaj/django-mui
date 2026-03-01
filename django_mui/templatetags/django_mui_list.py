from urllib.parse import urlencode

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def list_query(context, page):
    request = context.get("request")
    params = []
    if request is not None:
        search = request.GET.get("q", "").strip()
        ordering = request.GET.get("ordering", "").strip()
        page_size = request.GET.get("page_size", "").strip()
        if search:
            params.append(("q", search))
        if ordering:
            params.append(("ordering", ordering))
        if page_size.isdigit() and 1 <= int(page_size) <= 100:
            params.append(("page_size", page_size))
    params.append(("page", page))
    return urlencode(params)
