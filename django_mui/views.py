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


TODO_DASHBOARD_SESSION_KEY = "django_mui_demo_todos"
TODO_BRANDING_DEFAULT = "default"
TODO_BRANDING_PRESETS = {
    "default": {
        "label": "Default tokens",
        "description": "Uses the package defaults from django_mui.design_tokens.",
        "tokens": {},
    },
    "ocean": {
        "label": "Ocean",
        "description": "Blue accent with lighter surfaces.",
        "tokens": {
            "background": "#eef6ff",
            "surface": "#ffffff",
            "text-primary": "#0a2540",
            "accent": "#0066cc",
        },
    },
    "sunset": {
        "label": "Sunset",
        "description": "Warm accent with soft contrast for dashboards.",
        "tokens": {
            "background": "#fff8f1",
            "surface": "#ffffff",
            "text-primary": "#402218",
            "accent": "#d9480f",
        },
    },
}


def _get_demo_todos(request):
    stored_todos = request.session.get(TODO_DASHBOARD_SESSION_KEY, [])
    todos = []
    for item in stored_todos:
        if not isinstance(item, dict):
            continue
        try:
            todo_id = int(item.get("id"))
        except (TypeError, ValueError):
            continue
        title = str(item.get("title", "")).strip()
        if not title:
            continue
        todos.append({"id": todo_id, "title": title, "is_done": bool(item.get("is_done"))})
    return todos


def _save_demo_todos(request, todos):
    request.session[TODO_DASHBOARD_SESSION_KEY] = todos
    request.session.modified = True


def _get_branding_variables(branding_key):
    preset = TODO_BRANDING_PRESETS.get(branding_key, TODO_BRANDING_PRESETS[TODO_BRANDING_DEFAULT])
    token_items = sorted(preset.get("tokens", {}).items())
    return "; ".join(f"--django-mui-{token}: {value}" for token, value in token_items)


def example_index_view(request):
    return render(request, "django_mui/examples/index.html")


def example_todo_dashboard_view(request):
    selected_branding = request.GET.get("brand", TODO_BRANDING_DEFAULT)
    if selected_branding not in TODO_BRANDING_PRESETS:
        selected_branding = TODO_BRANDING_DEFAULT
    todos = _get_demo_todos(request)
    feedback_message = ""
    feedback_level = "info"
    if request.method == "POST":
        action = request.POST.get("action", "").strip()
        todo_title = request.POST.get("title", "").strip()
        todo_id_raw = request.POST.get("todo_id", "").strip()
        todo_id = None
        if todo_id_raw:
            try:
                todo_id = int(todo_id_raw)
            except ValueError:
                todo_id = None
        todo_lookup = {todo["id"]: todo for todo in todos}
        if action == "create":
            if not todo_title:
                feedback_level = "error"
                feedback_message = "Todo title is required."
            else:
                next_id = max((todo["id"] for todo in todos), default=0) + 1
                todos.append({"id": next_id, "title": todo_title, "is_done": False})
                feedback_level = "success"
                feedback_message = "Todo created."
        elif action == "update":
            if todo_id is None or todo_id not in todo_lookup:
                feedback_level = "error"
                feedback_message = "Selected todo no longer exists."
            elif not todo_title:
                feedback_level = "error"
                feedback_message = "Updated title is required."
            else:
                todo_lookup[todo_id]["title"] = todo_title
                feedback_level = "success"
                feedback_message = "Todo updated."
        elif action == "toggle":
            if todo_id is None or todo_id not in todo_lookup:
                feedback_level = "error"
                feedback_message = "Selected todo no longer exists."
            else:
                todo_lookup[todo_id]["is_done"] = not todo_lookup[todo_id]["is_done"]
                feedback_level = "success"
                feedback_message = "Todo status updated."
        elif action == "delete":
            if todo_id is None or todo_id not in todo_lookup:
                feedback_level = "error"
                feedback_message = "Selected todo no longer exists."
            else:
                todos = [todo for todo in todos if todo["id"] != todo_id]
                feedback_level = "success"
                feedback_message = "Todo deleted."
        else:
            feedback_level = "error"
            feedback_message = "Unsupported action."
        _save_demo_todos(request, todos)
    branding_options = [
        {
            "value": key,
            "label": preset["label"],
            "description": preset["description"],
        }
        for key, preset in TODO_BRANDING_PRESETS.items()
    ]
    completed_count = sum(1 for todo in todos if todo["is_done"])
    open_count = len(todos) - completed_count
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
                "label": "Todo dashboard",
                "url": reverse("django_mui_example_todo_dashboard"),
                "is_active": request.path == reverse("django_mui_example_todo_dashboard"),
            },
            {
                "label": "Design tokens",
                "url": reverse("django_mui_design_token_parity"),
                "is_active": request.path == reverse("django_mui_design_token_parity"),
            },
        ],
        "breadcrumbs": [
            {"label": "Examples", "url": reverse("django_mui_example_index")},
            {"label": "Todo dashboard", "active": True},
        ],
        "todos": sorted(todos, key=lambda item: item["id"]),
        "todo_feedback_message": feedback_message,
        "todo_feedback_level": feedback_level,
        "selected_branding": selected_branding,
        "branding_options": branding_options,
        "branding_variables_inline_style": _get_branding_variables(selected_branding),
        "branding_preview_tokens": TODO_BRANDING_PRESETS[selected_branding].get("tokens", {}),
        "todo_total_count": len(todos),
        "todo_open_count": open_count,
        "todo_completed_count": completed_count,
    }
    return render(request, "django_mui/examples/todo_dashboard.html", context)


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
    table_toolbar_actions = [
        {"label": "Create order", "url": "#create-order"},
        {"label": "Export CSV", "url": "#export-csv"},
        {"label": "Help", "url": "#table-help"},
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
    table_selection_summary = {
        "selected_count": len(selected_ids),
        "label": "order(s) selected",
        "clear_url": reverse("django_mui_example_integration"),
    }
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
                "label": "Todo dashboard",
                "url": reverse("django_mui_example_todo_dashboard"),
                "is_active": request.path == reverse("django_mui_example_todo_dashboard"),
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
        "table_toolbar_actions": table_toolbar_actions,
        "table_selection_summary": table_selection_summary,
        "table_saved_view_metadata": {
            "name": "Needs manager review",
            "owner": "manager@example.com",
        },
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
        "workflow_audit_banner": {
            "actor": "manager@example.com",
            "timestamp": datetime(2026, 1, 16, 8, 15, tzinfo=timezone.utc),
            "source": "Approval queue",
        },
        "workflow_transition_history": [
            {
                "action": "Submitted",
                "actor": "agent@example.com",
                "timestamp": datetime(2026, 1, 15, 10, 30, tzinfo=timezone.utc),
            },
            {
                "action": "Escalated",
                "actor": "manager@example.com",
                "timestamp": datetime(2026, 1, 16, 8, 0, tzinfo=timezone.utc),
            },
        ],
        "workflow_sla_summary": {
            "overdue_count": 1,
            "at_risk_count": 2,
            "on_time_count": 5,
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
