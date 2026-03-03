from datetime import datetime, timezone

from django import forms
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse

from django_mui.list_query import get_ordering_from_request, get_page_size_from_request


def design_token_parity_view(request):
    return render(request, "django_mui/design_token_parity.html")


class ExampleOrderFilterForm(forms.Form):
    q = forms.CharField(label="Search orders", required=False)
    ordering = forms.ChoiceField(
        label="Sort by",
        required=False,
        choices=(("order", "Order (ascending)"), ("-order", "Order (descending)")),
    )


def example_index_view(request):
    return render(request, "django_mui/examples/index.html")


def example_integration_view(request):
    allowed_orderings = ["order", "-order"]
    allowed_page_sizes = [2, 3]
    ordering = get_ordering_from_request(request, allowed_orderings, "order")
    page_size = get_page_size_from_request(request, allowed_page_sizes, 2)
    order_rows = [
        ["SO-1001", "Acme Co", "Pending"],
        ["SO-1002", "Globex", "Approved"],
        ["SO-1003", "Initech", "Shipped"],
    ]
    if ordering == "-order":
        order_rows = list(reversed(order_rows))
    paginator = Paginator(order_rows, per_page=page_size)
    page_obj = paginator.get_page(request.GET.get("page"))
    context = {
        "tab_items": [
            {
                "label": "Examples home",
                "url": reverse("django_mui_example_index"),
                "is_active": request.path == reverse("django_mui_example_index"),
            },
            {
                "label": "Integration",
                "url": reverse("django_mui_example_integration"),
                "is_active": request.path == reverse("django_mui_example_integration"),
            },
            {
                "label": "Design tokens",
                "url": reverse("django_mui_design_token_parity"),
                "is_active": request.path == reverse("django_mui_design_token_parity"),
            },
        ],
        "breadcrumbs": [
            {"label": "Examples", "url": reverse("django_mui_example_index")},
            {"label": "Integration", "active": True},
        ],
        "columns": ["Order", "Customer", "Status"],
        "allowed_page_sizes": allowed_page_sizes,
        "page_obj": page_obj,
        "rows": page_obj.object_list,
        "form": ExampleOrderFilterForm(request.GET),
        "workflow_payload": {
            "objectId": "SO-1001",
            "state": "pending",
            "allowedTransitions": ["approve", "reject"],
            "transitionUrl": reverse("django_mui_workflow_transition"),
        },
        "timeline_events": [
            {
                "status": "success",
                "status_label": "Created",
                "description": "Order SO-1001 created by admin.",
                "timestamp": datetime(2026, 1, 15, 9, 0, tzinfo=timezone.utc),
            },
            {
                "status": "info",
                "status_label": "Submitted",
                "description": "Order submitted for approval.",
                "timestamp": datetime(2026, 1, 15, 10, 30, tzinfo=timezone.utc),
            },
            {
                "status": "warning",
                "status_label": "Pending",
                "description": "Awaiting manager review.",
                "timestamp": datetime(2026, 1, 16, 8, 0, tzinfo=timezone.utc),
            },
        ],
        "nav_sections": [
            {
                "label": "Orders",
                "items": [
                    {
                        "label": "All orders",
                        "url": reverse("django_mui_example_integration"),
                        "is_active": True,
                    },
                    {
                        "label": "Pending approval",
                        "url": "#pending",
                        "is_active": False,
                    },
                ],
            },
            {
                "label": "Reports",
                "items": [
                    {
                        "label": "Monthly summary",
                        "url": "#monthly",
                        "is_active": False,
                    },
                ],
            },
        ],
    }
    return render(request, "django_mui/examples/integration.html", context)
