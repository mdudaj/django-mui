from django.urls import path

from django_mui.workflow import workflow_transition

urlpatterns = [
    path(
        "workflow/transition/",
        workflow_transition,
        name="django_mui_workflow_transition",
    ),
]
