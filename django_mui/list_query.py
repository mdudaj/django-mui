def resolve_ordering(ordering, allowed_orderings, default_ordering):
    if ordering in allowed_orderings:
        return ordering
    return default_ordering


def get_ordering_from_request(request, allowed_orderings, default_ordering):
    ordering = request.GET.get("ordering", "").strip()
    return resolve_ordering(ordering, allowed_orderings, default_ordering)


def resolve_page_size(page_size, allowed_page_sizes, default_page_size):
    try:
        parsed_page_size = int(page_size)
    except (TypeError, ValueError):
        return default_page_size
    if parsed_page_size in allowed_page_sizes:
        return parsed_page_size
    return default_page_size


def get_page_size_from_request(request, allowed_page_sizes, default_page_size):
    page_size = request.GET.get("page_size", "").strip()
    return resolve_page_size(page_size, allowed_page_sizes, default_page_size)


def resolve_filters(raw_filters, allowed_filters, defaults=None):
    """Validate and resolve multiple filter values.

    ``allowed_filters`` maps filter names to iterables of permitted values.
    Values not in the allowed set fall back to the corresponding entry in
    ``defaults`` (or are omitted when no default is given).
    """
    defaults = defaults or {}
    resolved = {}
    for name, allowed_values in allowed_filters.items():
        raw = raw_filters.get(name)
        if raw is not None and raw in allowed_values:
            resolved[name] = raw
        elif name in defaults:
            resolved[name] = defaults[name]
    return resolved


def get_filters_from_request(request, allowed_filters, defaults=None):
    """Extract and validate multiple filter parameters from the request."""
    raw_filters = {}
    for name in allowed_filters:
        value = request.GET.get(name, "").strip()
        if value:
            raw_filters[name] = value
    return resolve_filters(raw_filters, allowed_filters, defaults)
