from django.conf import settings
from django.urls import NoReverseMatch, reverse


def get_navigation_registry():
    return list(getattr(settings, "DJANGO_MUI_NAVIGATION", []))


def _user_has_permissions(user, required_permissions):
    if not required_permissions:
        return True
    if user is None:
        return False
    has_perms = getattr(user, "has_perms", None)
    if has_perms is None:
        return False
    return has_perms(required_permissions)


def _resolve_url(route_name):
    if not route_name:
        return "#"
    try:
        return reverse(route_name)
    except NoReverseMatch:
        return "#"


def _is_route_active(
    route_name,
    active_view_name,
    active_view_prefixes,
    request_path,
    active_path_prefixes,
):
    if any(request_path.startswith(prefix) for prefix in active_path_prefixes if prefix):
        return True
    if active_view_name is None:
        return False
    if route_name and route_name == active_view_name:
        return True
    return any(
        active_view_name.startswith(prefix)
        for prefix in active_view_prefixes
        if prefix
    )


def _build_item(item, user, active_view_name, request_path):
    required_permissions = list(item.get("required_permissions", []))
    if not _user_has_permissions(user, required_permissions):
        return None

    children = []
    for child in item.get("children", []):
        built_child = _build_item(child, user, active_view_name, request_path)
        if built_child is not None:
            children.append(built_child)

    route_name = item.get("route_name")
    active_view_prefixes = list(item.get("active_view_prefixes", []))
    active_path_prefixes = list(item.get("active_path_prefixes", []))
    is_active = _is_route_active(
        route_name,
        active_view_name,
        active_view_prefixes,
        request_path,
        active_path_prefixes,
    ) or any(
        child["active"] for child in children
    )

    return {
        "id": item.get("id"),
        "label": item.get("label"),
        "route_name": route_name,
        "icon": item.get("icon"),
        "required_permissions": required_permissions,
        "active_view_prefixes": active_view_prefixes,
        "active_path_prefixes": active_path_prefixes,
        "children": children,
        "url": _resolve_url(route_name),
        "active": is_active,
    }


def build_navigation(request, registry=None):
    navigation_registry = registry if registry is not None else get_navigation_registry()
    resolver_match = getattr(request, "resolver_match", None)
    active_view_name = getattr(resolver_match, "view_name", None)
    request_path = getattr(request, "path", "")
    user = getattr(request, "user", None)

    built_navigation = []
    for item in navigation_registry:
        built_item = _build_item(item, user, active_view_name, request_path)
        if built_item is not None:
            built_navigation.append(built_item)
    return built_navigation
