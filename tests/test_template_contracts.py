import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]


class TemplateContractTests(unittest.TestCase):
    def test_base_template_includes_messages_and_breadcrumbs_partials(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/base.html"
        ).read_text(encoding="utf-8")
        self.assertIn('{% include "django_mui/includes/messages.html" %}', content)
        self.assertIn('{% include "django_mui/includes/breadcrumbs.html" %}', content)

    def test_messages_partial_maps_expected_levels(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/includes/messages.html"
        ).read_text(encoding="utf-8")
        self.assertIn("message.level_tag == 'success'", content)
        self.assertIn("message.level_tag == 'warning'", content)
        self.assertIn("message.level_tag == 'error'", content)
        self.assertIn("mui-alert-info", content)

    def test_breadcrumbs_partial_exposes_aria_current(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/includes/breadcrumbs.html"
        ).read_text(encoding="utf-8")
        self.assertIn('aria-label="Breadcrumb"', content)
        self.assertIn('aria-current="page"', content)


if __name__ == "__main__":
    unittest.main()
