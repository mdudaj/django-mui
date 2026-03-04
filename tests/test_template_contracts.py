import unittest
from pathlib import Path

from django.conf import settings
from django.template import Context, Engine


BASE_DIR = Path(__file__).resolve().parents[1]

if not settings.configured:
    settings.configure(USE_I18N=False)


class TemplateContractTests(unittest.TestCase):
    def test_base_template_includes_messages_and_breadcrumbs_partials(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/base.html"
        ).read_text(encoding="utf-8")
        self.assertIn("django_mui/base.css", content)
        self.assertIn('{% include "django_mui/includes/messages.html" %}', content)
        self.assertIn('{% include "django_mui/includes/breadcrumbs.html" %}', content)

    def test_base_stylesheet_defines_alert_styles(self):
        content = (BASE_DIR / "django_mui/static/django_mui/base.css").read_text(
            encoding="utf-8"
        )
        self.assertIn(".mui-alert", content)
        self.assertIn(".mui-alert-success", content)

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
        self.assertIn("{% if bulk_actions %}<form method=\"post\"", content)
        self.assertIn('name="selected_ids"', content)
        self.assertIn('row_identifier=row.id|default:forloop.counter0|stringformat:"s"', content)
        self.assertIn("row_identifier in selected_ids", content)
        self.assertIn("row.cells|default:row", content)
        self.assertIn("bulk_action_feedback", content)
        self.assertIn('role="{% if bulk_action_feedback_level == \'error\' %}alert{% else %}status{% endif %}"', content)
        self.assertIn('{% if table_rows %}', content)
        self.assertIn('empty_label|default:"No records found."', content)
        self.assertIn('aria-label="Pagination"', content)
        self.assertIn("list_query page_obj.previous_page_number", content)
        self.assertIn("list_query page_obj.next_page_number", content)

    def test_form_error_summary_partial_renders_non_field_and_field_errors(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/includes/form_error_summary.html"
        ).read_text(encoding="utf-8")
        self.assertIn("{% if form and form.errors %}", content)
        self.assertIn("form.non_field_errors", content)
        self.assertIn("form.visible_fields", content)
        self.assertIn('role="alert"', content)
        self.assertIn('aria-labelledby="mui-form-error-summary-title"', content)
        self.assertNotIn('aria-live="assertive"', content)

    def test_tabs_partial_renders_context_items_and_active_state(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/includes/tabs.html"
        ).read_text(encoding="utf-8")
        self.assertIn("{% if tab_items %}", content)
        self.assertIn("{% for tab in tab_items %}", content)
        self.assertIn("tab.is_active", content)
        self.assertIn('aria-current="page"', content)

    def test_example_integration_template_covers_form_workflow_and_table_patterns(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/examples/integration.html"
        ).read_text(encoding="utf-8")
        self.assertIn('{% extends "django_mui/base.html" %}', content)
        self.assertIn(
            '{% include "django_mui/includes/tabs.html" with tab_items=tab_items tabs_aria_label="Example pages" %}',
            content,
        )
        self.assertIn(
            '{% include "django_mui/includes/form_error_summary.html" with form=form %}',
            content,
        )
        self.assertIn("{% render_form_field form.q %}", content)
        self.assertIn("{% render_form_field form.ordering %}", content)
        self.assertIn(
            '{% include "django_mui/includes/workflow_transitions.html" with workflow_transitions=workflow_transitions %}',
            content,
        )
        self.assertIn(
            '{% include "django_mui/includes/table.html" with columns=columns page_obj=page_obj bulk_form_action=bulk_form_action bulk_actions=bulk_actions selected_ids=selected_ids bulk_action_feedback=bulk_action_feedback bulk_action_feedback_level=bulk_action_feedback_level %}',
            content,
        )

    def test_urls_include_example_entry_points(self):
        content = (BASE_DIR / "django_mui/urls.py").read_text(encoding="utf-8")
        self.assertIn("django_mui_example_index", content)
        self.assertIn("django_mui_example_integration", content)

    def test_example_view_provides_table_rows_and_workflow_endpoint_context(self):
        content = (BASE_DIR / "django_mui/views.py").read_text(encoding="utf-8")
        self.assertIn("get_ordering_from_request", content)
        self.assertIn("get_page_size_from_request", content)
        self.assertIn("current_nav_item = {", content)
        self.assertIn('"tab_items": [', content)
        self.assertIn('"is_active": request.path == reverse("django_mui_example_integration")', content)
        self.assertIn('{"label": current_nav_item["label"], "active": True}', content)
        self.assertIn('allowed_orderings = ["order", "-order"]', content)
        self.assertIn("allowed_page_sizes = [2, 3]", content)
        self.assertIn('"rows": page_obj.object_list', content)
        self.assertIn('"bulk_form_action": reverse("django_mui_example_integration")', content)
        self.assertIn('"bulk_actions": bulk_actions', content)
        self.assertIn('"selected_ids": selected_ids', content)
        self.assertIn('"bulk_action_feedback": bulk_action_feedback', content)
        self.assertIn('"bulk_action_feedback_level": bulk_action_feedback_level', content)
        self.assertIn('bulk_action_feedback = "Select at least one order to apply a bulk action."', content)
        self.assertIn('bulk_action_feedback = "Some selected orders are no longer available."', content)
        self.assertIn('bulk_action_feedback = "Selected bulk action is unavailable."', content)
        self.assertIn('reverse("django_mui_workflow_transition")', content)
        self.assertIn('"workflow_transitions": [', content)
        self.assertIn('"is_disabled": True', content)
        self.assertIn('"disabled_reason": "Rejection requires manager override."', content)

    def test_readme_links_example_entry_points(self):
        content = (BASE_DIR / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Example integration pages", content)
        self.assertIn("django_mui_example_index", content)
        self.assertIn("django_mui_example_integration", content)

    def test_timeline_partial_renders_events_with_status_and_timestamp(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/includes/timeline.html"
        ).read_text(encoding="utf-8")
        self.assertIn("{% if timeline_groups %}", content)
        self.assertIn("{% for group in timeline_groups %}", content)
        self.assertIn("group.label", content)
        self.assertIn("{% for event in group.events %}", content)
        self.assertIn("{% elif timeline_events %}", content)
        self.assertIn("{% for event in timeline_events %}", content)
        self.assertIn("event.status", content)
        self.assertIn("event.description", content)
        self.assertIn("event.timestamp", content)
        self.assertIn("mui-timeline", content)
        self.assertIn('aria-label="', content)
        self.assertIn("timeline_empty_label", content)

    def test_base_stylesheet_defines_timeline_styles(self):
        content = (BASE_DIR / "django_mui/static/django_mui/base.css").read_text(
            encoding="utf-8"
        )
        self.assertIn(".mui-timeline", content)
        self.assertIn(".mui-timeline-event", content)

    def test_example_integration_template_includes_timeline_section(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/examples/integration.html"
        ).read_text(encoding="utf-8")
        self.assertIn(
            '{% include "django_mui/includes/timeline.html" with timeline_groups=timeline_groups %}',
            content,
        )
        self.assertIn(
            '{% include "django_mui/includes/timeline.html" with timeline_events=empty_timeline_events timeline_empty_label="No workflow activity yet." %}',
            content,
        )

    def test_example_view_provides_timeline_events_context(self):
        content = (BASE_DIR / "django_mui/views.py").read_text(encoding="utf-8")
        self.assertIn('"timeline_events":', content)
        self.assertIn('"timeline_groups":', content)
        self.assertIn('"events": [', content)
        self.assertIn('"empty_timeline_events": []', content)
        self.assertIn('"status":', content)
        self.assertIn('"status_label":', content)
        self.assertIn('"description":', content)
        self.assertIn('"timestamp":', content)

    def test_nav_section_partial_renders_groups_with_accessible_labels(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/includes/nav_section.html"
        ).read_text(encoding="utf-8")
        self.assertIn("{% if nav_sections %}", content)
        self.assertIn("{% for section in nav_sections %}", content)
        self.assertIn("section.label", content)
        self.assertIn("{% for item in section.items %}", content)
        self.assertIn("item.url", content)
        self.assertIn("item.is_active", content)
        self.assertIn("item.is_unavailable", content)
        self.assertIn('role="link"', content)
        self.assertIn('aria-disabled="true"', content)
        self.assertIn("aria-describedby=", content)
        self.assertIn('default:"Unavailable with current permissions."', content)
        self.assertIn('aria-current="page"', content)
        self.assertIn('role="group"', content)
        self.assertIn("aria-labelledby=", content)
        self.assertIn("mui-nav-section", content)

    def test_base_stylesheet_defines_nav_section_styles(self):
        content = (BASE_DIR / "django_mui/static/django_mui/base.css").read_text(
            encoding="utf-8"
        )
        self.assertIn(".mui-nav-section", content)
        self.assertIn(".mui-nav-section__label", content)
        self.assertIn(".mui-nav-section__items", content)

    def test_workflow_transitions_partial_supports_disabled_reason_contract(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/includes/workflow_transitions.html"
        ).read_text(encoding="utf-8")
        self.assertIn("{% if workflow_transitions %}", content)
        self.assertIn("{% for transition in workflow_transitions %}", content)
        self.assertIn("transition.is_disabled", content)
        self.assertIn("transition.disabled_reason", content)
        self.assertIn("disabled", content)
        self.assertIn("aria-describedby=", content)
        self.assertIn("mui-workflow-transition-reason-", content)
        self.assertIn('default:"Transition unavailable."', content)

    def test_base_stylesheet_defines_workflow_transition_styles(self):
        content = (BASE_DIR / "django_mui/static/django_mui/base.css").read_text(
            encoding="utf-8"
        )
        self.assertIn(".mui-workflow-transitions", content)
        self.assertIn(".mui-workflow-transitions__item", content)
        self.assertIn(".mui-workflow-transitions__reason", content)

    def test_example_integration_template_includes_nav_section(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/examples/integration.html"
        ).read_text(encoding="utf-8")
        self.assertIn(
            '{% include "django_mui/includes/nav_section.html" with nav_sections=nav_sections %}',
            content,
        )

    def test_example_view_provides_nav_sections_context(self):
        content = (BASE_DIR / "django_mui/views.py").read_text(encoding="utf-8")
        self.assertIn('"nav_sections":', content)
        self.assertIn('"is_active": request.path == current_nav_item["url"]', content)
        self.assertIn('"is_unavailable": True', content)
        self.assertIn('"unavailable_reason": "Requires reports.view_monthly permission."', content)

    def test_nav_section_partial_renders_default_unavailable_reason(self):
        content = (
            BASE_DIR / "django_mui/templates/django_mui/includes/nav_section.html"
        ).read_text(encoding="utf-8")
        rendered = Engine().from_string(content).render(
            Context(
                {
                    "nav_sections": [
                        {
                            "label": "Reports",
                            "items": [{"label": "Monthly summary", "is_unavailable": True}],
                        }
                    ]
                }
            )
        )
        self.assertIn("Unavailable with current permissions.", rendered)

    def test_implementation_backlog_tracks_open_and_completed_phases(self):
        content = (BASE_DIR / "docs/implementation-issues.md").read_text(encoding="utf-8")
        self.assertIn("## Phase 8 Backlog (Open)", content)
        self.assertIn("Add navigation permission-guard contract", content)
        self.assertIn("Add workflow timeline grouping contract", content)
        self.assertIn("## Phase 7 Backlog (Completed)", content)
        self.assertIn("Add workflow transition guard contract", content)
        self.assertIn("Add server-rendered table bulk-actions contract", content)
        self.assertIn("Add navigation + breadcrumb composition contract", content)
        self.assertIn("## Phase 6 Backlog (Completed)", content)
        self.assertIn("Add workflow activity timeline contract", content)
        self.assertIn("Add advanced list/table server query contract", content)
        self.assertIn("Add nested navigation section rendering contract", content)
        self.assertIn("## Phase 5 Backlog (Completed)", content)
        self.assertIn("Phase 5 backlog items are complete", content)
        self.assertIn("Add SSR-first form error summary partial", content)
        self.assertIn("Add server-side tabs navigation template contract", content)
        self.assertIn("Add pagination page-size query helper", content)
        self.assertIn("Document feature parity matrix by maturity level", content)
        self.assertIn("Phase 3 backlog items are also complete", content)
        self.assertIn("## Phase 4 Backlog (Completed)", content)
        self.assertIn("Phase 4 backlog items are complete", content)
        self.assertIn(
            "Improve navigation active-state matching for nested routes",
            content,
        )
        self.assertIn(
            "Improve navigation active-state matching for URL path prefixes",
            content,
        )

    def test_feature_inventory_documents_maturity_parity_matrix(self):
        inventory = (BASE_DIR / "docs/feature-inventory.md").read_text(encoding="utf-8")
        readme = (BASE_DIR / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Feature parity matrix by maturity tier", inventory)
        self.assertIn("Implemented", inventory)
        self.assertIn("Planned", inventory)
        self.assertIn("Out of scope", inventory)
        self.assertIn("Feature parity maturity tracking is documented", readme)


if __name__ == "__main__":
    unittest.main()
