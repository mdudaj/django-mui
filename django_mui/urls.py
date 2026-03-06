from django.urls import path

from django_mui.views import (
    design_token_parity_view,
    example_index_view,
    example_integration_view,
    example_todo_dashboard_view,
)
from django_mui.workflow import workflow_transition

urlpatterns = [
    path("examples/", example_index_view, name="django_mui_example_index"),
    path(
        "examples/integration/",
        example_integration_view,
        name="django_mui_example_integration",
    ),
    path(
        "examples/todo-dashboard/",
        example_todo_dashboard_view,
        name="django_mui_example_todo_dashboard",
    ),
    path(
        "design-tokens/parity/",
        design_token_parity_view,
        name="django_mui_design_token_parity",
    ),
    path(
        "workflow/transition/",
        workflow_transition,
        name="django_mui_workflow_transition",
    ),
]
