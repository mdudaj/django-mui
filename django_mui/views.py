from django import forms
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse

from django_mui.list_query import get_ordering_from_request


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
    ordering = get_ordering_from_request(request, allowed_orderings, "order")
    order_rows = [
        ["SO-1001", "Acme Co", "Pending"],
        ["SO-1002", "Globex", "Approved"],
        ["SO-1003", "Initech", "Shipped"],
    ]
    if ordering == "-order":
        order_rows = list(reversed(order_rows))
    paginator = Paginator(order_rows, per_page=2)
    page_obj = paginator.get_page(request.GET.get("page"))
    context = {
        "breadcrumbs": [
            {"label": "Examples", "url": reverse("django_mui_example_index")},
            {"label": "Integration", "active": True},
        ],
        "columns": ["Order", "Customer", "Status"],
        "page_obj": page_obj,
        "rows": page_obj.object_list,
        "form": ExampleOrderFilterForm(request.GET),
        "workflow_payload": {
            "objectId": "SO-1001",
            "state": "pending",
            "allowedTransitions": ["approve", "reject"],
            "transitionUrl": reverse("django_mui_workflow_transition"),
        },
    }
    return render(request, "django_mui/examples/integration.html", context)
