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

    def test_example_integration_template_covers_form_workflow_and_table_patterns(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/examples/integration.html"
        ).read_text(encoding="utf-8")
        self.assertIn('{% extends "django_mui/base.html" %}', content)
        self.assertIn("{% render_form_field form.q %}", content)
        self.assertIn("{% render_form_field form.ordering %}", content)
        self.assertIn("{% url 'django_mui_workflow_transition' %}", content)
        self.assertIn(
            '{% include "django_mui/includes/table.html" with columns=columns page_obj=page_obj %}',
            content,
        )

    def test_urls_include_example_entry_points(self):
        content = (BASE_DIR / "django_mui/urls.py").read_text(encoding="utf-8")
        self.assertIn("django_mui_example_index", content)
        self.assertIn("django_mui_example_integration", content)

    def test_example_view_provides_table_rows_and_workflow_endpoint_context(self):
        content = (BASE_DIR / "django_mui/views.py").read_text(encoding="utf-8")
        self.assertIn("get_ordering_from_request", content)
        self.assertIn('allowed_orderings = ["order", "-order"]', content)
        self.assertIn('"rows": page_obj.object_list', content)
        self.assertIn('reverse("django_mui_workflow_transition")', content)

    def test_readme_links_example_entry_points(self):
        content = (BASE_DIR / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Example integration pages", content)
        self.assertIn("django_mui_example_index", content)
        self.assertIn("django_mui_example_integration", content)

    def test_implementation_backlog_marks_phase_3_complete(self):
        content = (BASE_DIR / "docs/implementation-issues.md").read_text(encoding="utf-8")
        self.assertIn("Phase 3 backlog items are also complete", content)
        self.assertIn("## Phase 4 Backlog (Current)", content)
        self.assertIn(
            "Improve navigation active-state matching for nested routes",
            content,
        )
        self.assertIn(
            "Improve navigation active-state matching for URL path prefixes",
            content,
        )


if __name__ == "__main__":
    unittest.main()
