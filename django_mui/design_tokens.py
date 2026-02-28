TOKEN_SOURCE = {
    "color": {
        "background": {"light": "#ffffff", "dark": "#121212"},
        "surface": {"light": "#f7f7f8", "dark": "#1e1e1e"},
        "text_primary": {"light": "#1f2937", "dark": "#f3f4f6"},
        "accent": {"light": "#1976d2", "dark": "#90caf9"},
    }
}


def _normalize_mode(mode):
    return "dark" if mode == "dark" else "light"


def get_token_values(mode="light"):
    active_mode = _normalize_mode(mode)
    values = {}
    for token_name, token_modes in TOKEN_SOURCE["color"].items():
        if active_mode not in token_modes:
            raise KeyError(f"Token '{token_name}' is missing mode \"{active_mode}\".")
        values[token_name] = token_modes[active_mode]
    return values


def get_css_variables(mode="light"):
    values = get_token_values(mode)
    return {f"--django-mui-{name.replace('_', '-')}": value for name, value in values.items()}


def get_mui_theme_tokens(mode="light"):
    values = get_token_values(mode)
    active_mode = _normalize_mode(mode)
    return {
        "palette": {
            "mode": active_mode,
            "background": {
                "default": values["background"],
                "paper": values["surface"],
            },
            "text": {"primary": values["text_primary"]},
            "primary": {"main": values["accent"]},
        }
    }
