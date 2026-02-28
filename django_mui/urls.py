from django.urls import path

from django_mui.views import design_token_parity_view
from django_mui.workflow import workflow_transition

urlpatterns = [
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
