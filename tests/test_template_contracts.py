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

    def test_table_partial_supports_rows_empty_state_and_pagination(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/includes/table.html"
        ).read_text(encoding="utf-8")
        self.assertIn("{% load django_mui_list %}", content)
        self.assertIn("table_rows=page_obj.object_list|default:rows", content)
        self.assertIn('{% if table_rows %}', content)
        self.assertIn('empty_label|default:"No records found."', content)
        self.assertIn('aria-label="Pagination"', content)
        self.assertIn("list_query page_obj.previous_page_number", content)
        self.assertIn("list_query page_obj.next_page_number", content)


if __name__ == "__main__":
    unittest.main()
