def resolve_ordering(ordering, allowed_orderings, default_ordering):
    if ordering in allowed_orderings:
        return ordering
    return default_ordering


def get_ordering_from_request(request, allowed_orderings, default_ordering):
    ordering = request.GET.get("ordering", "").strip()
    return resolve_ordering(ordering, allowed_orderings, default_ordering)
