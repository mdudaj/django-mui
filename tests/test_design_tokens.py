import unittest

from django_mui.design_tokens import get_css_variables, get_mui_theme_tokens, get_token_values


class DesignTokenTests(unittest.TestCase):
    def test_get_token_values_defaults_to_light_mode(self):
        self.assertEqual(get_token_values("unsupported")["background"], "#ffffff")

    def test_get_css_variables_uses_expected_prefix(self):
        css_variables = get_css_variables("dark")
        self.assertEqual(css_variables["--django-mui-background"], "#121212")
        self.assertIn("--django-mui-text-primary", css_variables)

    def test_get_mui_theme_tokens_matches_mode(self):
        theme_tokens = get_mui_theme_tokens("dark")
        self.assertEqual(theme_tokens["palette"]["mode"], "dark")
        self.assertEqual(theme_tokens["palette"]["primary"]["main"], "#90caf9")
