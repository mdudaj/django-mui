from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, PermissionDenied, ValidationError
from django.http import JsonResponse
from django.utils.module_loading import import_string
from django.views.decorators.http import require_POST


def _default_response(ok=False, state=None, allowed_transitions=None, messages=None):
    return {
        "ok": bool(ok),
        "state": state,
        "allowed_transitions": list(allowed_transitions or []),
        "messages": list(messages or []),
    }


def _get_transition_handler():
    handler = getattr(settings, "DJANGO_MUI_WORKFLOW_TRANSITION_HANDLER", None)
    if isinstance(handler, str):
        return import_string(handler)
    return handler


@require_POST
def workflow_transition(request):
    transition = (request.POST.get("transition") or "").strip()
    object_id = (request.POST.get("object_id") or "").strip()

    if not transition or not object_id:
        return JsonResponse(
            _default_response(messages=["Missing transition or object_id."]),
            status=400,
        )
    try:
        object_id = int(object_id)
    except (TypeError, ValueError):
        return JsonResponse(_default_response(messages=["Invalid object_id."]), status=400)

    handler = _get_transition_handler()
    if handler is None:
        raise ImproperlyConfigured(
            "DJANGO_MUI_WORKFLOW_TRANSITION_HANDLER must be configured."
        )

    try:
        result = handler(request=request, transition=transition, object_id=object_id)
    except PermissionDenied:
        return JsonResponse(
            _default_response(messages=["You do not have permission to transition this object."]),
            status=403,
        )
    except ValidationError as exc:
        return JsonResponse(
            _default_response(messages=exc.messages or [str(exc)]),
            status=400,
        )

    if not isinstance(result, dict):
        raise ImproperlyConfigured(
            "DJANGO_MUI_WORKFLOW_TRANSITION_HANDLER must return a dictionary."
        )

    payload = _default_response(
        ok=result.get("ok"),
        state=result.get("state"),
        allowed_transitions=result.get("allowed_transitions"),
        messages=result.get("messages"),
    )
    return JsonResponse(payload, status=200 if payload["ok"] else 400)
