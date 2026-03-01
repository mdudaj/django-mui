from urllib.parse import urlencode

from django import template
from django_mui.list_query import resolve_page_size

register = template.Library()
MAX_PAGE_SIZE = 100
DEFAULT_ALLOWED_PAGE_SIZES = (10, 25, 50, MAX_PAGE_SIZE)


@register.simple_tag(takes_context=True)
def list_query(context, page):
    request = context.get("request")
    params = []
    if request is not None:
        search = request.GET.get("q", "").strip()
        ordering = request.GET.get("ordering", "").strip()
        page_size = request.GET.get("page_size", "").strip()
        context_page_sizes = context.get("allowed_page_sizes")
        allowed_page_sizes = (
            DEFAULT_ALLOWED_PAGE_SIZES
            if context_page_sizes is None
            else context_page_sizes
        )
        if search:
            params.append(("q", search))
        if ordering:
            params.append(("ordering", ordering))
        resolved_page_size = resolve_page_size(page_size, allowed_page_sizes, None)
        if resolved_page_size is not None:
            params.append(("page_size", str(resolved_page_size)))
    params.append(("page", page))
    return urlencode(params)
