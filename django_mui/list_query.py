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
