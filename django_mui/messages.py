def get_snackbar_messages_payload(messages):
    """Map Django message objects to a deterministic snackbar payload list."""
    level_map = {
        "success": "success",
        "warning": "warning",
        "error": "error",
    }
    payload = []
    for message in list(messages or []):
        level_tag = getattr(message, "level_tag", "") or "info"
        payload.append(
            {
                "level": level_tag,
                "severity": level_map.get(level_tag, "info"),
                "message": str(message),
            }
        )
    return payload
