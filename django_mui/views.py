from datetime import datetime, timezone

from django import forms
from django.contrib.messages import constants as message_constants
from django.contrib.messages.storage.base import Message
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse

from django_mui.list_query import get_ordering_from_request, get_page_size_from_request
from django_mui.messages import get_snackbar_messages_payload


def design_token_parity_view(request):
    return render(request, "django_mui/design_token_parity.html")


class ExampleOrderFilterForm(forms.Form):
    DEFAULT_ORDERING = "order"
    ORDERING_CHOICES = (("order", "Order (ascending)"), ("-order", "Order (descending)"))

    q = forms.CharField(label="Search orders", required=False)
    ordering = forms.ChoiceField(
        label="Sort by",
        required=False,
        choices=ORDERING_CHOICES,
    )

    @classmethod
    def get_ordering_label(cls, value):
        return dict(cls.ORDERING_CHOICES).get(value)


def example_index_view(request):
    return render(request, "django_mui/examples/index.html")


def example_integration_view(request):
    allowed_orderings = ["order", "-order"]
    allowed_page_sizes = [2, 3]
    search_filter = request.GET.get("q", "").strip()
    ordering = get_ordering_from_request(
        request,
        allowed_orderings,
        ExampleOrderFilterForm.DEFAULT_ORDERING,
    )
    page_size = get_page_size_from_request(request, allowed_page_sizes, 2)
    order_rows = [
        {
            "id": "SO-1001",
            "cells": ["SO-1001", "Acme Co", "Pending"],
            "state_badge": {"state": "warning", "label": "Needs review"},
        },
        {"id": "SO-1002", "cells": ["SO-1002", "Globex", "Approved"]},
        {
            "id": "SO-1003",
            "cells": ["SO-1003", "Initech", "Shipped"],
            "state_badge": {"state": "info", "label": "New"},
        },
    ]
    if ordering == "-order":
        order_rows = list(reversed(order_rows))
    bulk_actions = [
        {"value": "approve", "label": "Approve selected orders"},
        {"value": "archive", "label": "Archive selected orders"},
    ]
    selected_ids = [value.strip() for value in request.POST.getlist("selected_ids") if value.strip()]
    bulk_action_feedback = ""
    bulk_action_feedback_level = ""
    if request.method == "POST":
        valid_ids = {row["id"] for row in order_rows}
        has_invalid_ids = any(selected_id not in valid_ids for selected_id in selected_ids)
        action = request.POST.get("bulk_action", "").strip()
        allowed_actions = {item["value"] for item in bulk_actions}
        if not selected_ids:
            bulk_action_feedback = "Select at least one order to apply a bulk action."
            bulk_action_feedback_level = "error"
        elif has_invalid_ids:
            bulk_action_feedback = "Some selected orders are no longer available."
            bulk_action_feedback_level = "error"
        elif action not in allowed_actions:
            bulk_action_feedback = "Selected bulk action is unavailable."
            bulk_action_feedback_level = "error"
        else:
            bulk_action_feedback = f"Bulk action queued for {len(selected_ids)} order(s)."
            bulk_action_feedback_level = "success"
    paginator = Paginator(order_rows, per_page=page_size)
    page_obj = paginator.get_page(request.GET.get("page"))
    pagination_summary = {
        "start": page_obj.start_index(),
        "end": page_obj.end_index(),
        "total": paginator.count,
        "label": "orders",
    }
    current_nav_item = {
        "label": "All orders",
        "url": reverse("django_mui_example_integration"),
    }
    demo_messages = [
        Message(message_constants.SUCCESS, "Filters loaded with server-rendered fallback alerts."),
        Message(
            message_constants.INFO,
            "Optional snackbar payload is available for client islands.",
        ),
    ]
    active_filter_summary = []
    if search_filter:
        active_filter_summary.append({"label": "Search", "value": search_filter})
    ordering_label = ExampleOrderFilterForm.get_ordering_label(ordering)
    if ordering_label and ordering != ExampleOrderFilterForm.DEFAULT_ORDERING:
        active_filter_summary.append({"label": "Sort by", "value": ordering_label})
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
            {"label": current_nav_item["label"], "active": True},
        ],
        "columns": [
            {
                "label": "Order",
                "is_emphasis": True,
                "semantic_label": "Sales order number",
            },
            {"label": "Customer"},
            {"label": "Status", "align": "center", "semantic_label": "Order status"},
        ],
        "allowed_page_sizes": allowed_page_sizes,
        "page_obj": page_obj,
        "rows": page_obj.object_list,
        "bulk_form_action": reverse("django_mui_example_integration"),
        "bulk_actions": bulk_actions,
        "selected_ids": selected_ids,
        "bulk_action_feedback": bulk_action_feedback,
        "bulk_action_feedback_level": bulk_action_feedback_level,
        "active_filter_summary": active_filter_summary,
        "active_filter_reset_url": reverse("django_mui_example_integration"),
        "pagination_summary": pagination_summary,
        "form": ExampleOrderFilterForm(request.GET),
        "q_field_island": {
            "component": "FormFieldWidgetHint",
            "props": {
                "message": "Optional island metadata can enhance this field.",
            },
        },
        "messages": demo_messages,
        "snackbar_messages_payload": get_snackbar_messages_payload(demo_messages),
        "workflow_payload": {
            "objectId": "SO-1001",
            "state": "pending",
            "allowedTransitions": ["approve", "reject"],
            "transitionUrl": reverse("django_mui_workflow_transition"),
        },
        "workflow_transitions": [
            {
                "name": "approve",
                "label": "Approve example order",
                "url": reverse("django_mui_workflow_transition"),
                "object_id": "SO-1001",
                "is_disabled": False,
            },
            {
                "name": "reject",
                "label": "Reject example order",
                "url": reverse("django_mui_workflow_transition"),
                "object_id": "SO-1001",
                "is_disabled": True,
                "disabled_reason": "Rejection requires manager override.",
            },
        ],
        "workflow_status_summary": {
            "current_state": "pending",
            "current_state_label": "Pending manager approval",
            "next_steps": [
                {"label": "Approve order", "metadata": "Available to managers."},
                {"label": "Reject order", "metadata": "Requires manager override."},
            ],
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
        "timeline_groups": [
            {
                "label": "2026-01-15",
                "events": [
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
                ],
            },
            {
                "label": "2026-01-16",
                "events": [
                    {
                        "status": "warning",
                        "status_label": "Pending",
                        "description": "Awaiting manager review.",
                        "timestamp": datetime(2026, 1, 16, 8, 0, tzinfo=timezone.utc),
                    },
                ],
            },
        ],
        "empty_timeline_events": [],
        "nav_sections": [
            {
                "label": "Orders",
                "items": [
                    {
                        "label": current_nav_item["label"],
                        "url": current_nav_item["url"],
                        "is_active": request.path == current_nav_item["url"],
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
                        "is_unavailable": True,
                        "unavailable_reason": "Requires reports.view_monthly permission.",
                    },
                ],
            },
        ],
    }
    return render(request, "django_mui/examples/integration.html", context)
