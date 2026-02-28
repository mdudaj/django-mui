import json
import unittest
from unittest.mock import Mock, patch

from django.conf import settings
from django.core.exceptions import PermissionDenied, ValidationError

from django_mui.workflow import workflow_transition

if not settings.configured:
    settings.configure(
        DEFAULT_CHARSET="utf-8",
        ALLOWED_HOSTS=["*"],
    )


class WorkflowTransitionTests(unittest.TestCase):
    def test_workflow_transition_returns_400_for_missing_fields(self):
        request = Mock(method="POST", POST={"transition": "   ", "object_id": "   "})

        response = workflow_transition(request)

        self.assertEqual(response.status_code, 400)
        payload = json.loads(response.content)
        self.assertEqual(payload["messages"], ["Missing transition or object_id."])

    def test_workflow_transition_passes_stripped_object_id_to_handler(self):
        request = Mock(method="POST", POST={"transition": " approve ", "object_id": " 00123 "})
        handler = Mock(
            return_value={
                "ok": True,
                "state": "approved",
                "allowed_transitions": [],
                "messages": [],
            }
        )

        with patch("django_mui.workflow._get_transition_handler", return_value=handler):
            response = workflow_transition(request)

        self.assertEqual(response.status_code, 200)
        handler.assert_called_once()
        _, kwargs = handler.call_args
        self.assertEqual(kwargs["request"], request)
        self.assertEqual(kwargs["transition"], "approve")
        self.assertEqual(kwargs["object_id"], "00123")

    def test_workflow_transition_maps_permission_denied_to_403(self):
        request = Mock(method="POST", POST={"transition": "approve", "object_id": "123"})
        handler = Mock(side_effect=PermissionDenied)

        with patch("django_mui.workflow._get_transition_handler", return_value=handler):
            response = workflow_transition(request)

        self.assertEqual(response.status_code, 403)
        payload = json.loads(response.content)
        self.assertFalse(payload["ok"])

    def test_workflow_transition_maps_validation_error_to_400(self):
        request = Mock(method="POST", POST={"transition": "approve", "object_id": "123"})
        handler = Mock(side_effect=ValidationError(["invalid transition"]))

        with patch("django_mui.workflow._get_transition_handler", return_value=handler):
            response = workflow_transition(request)

        self.assertEqual(response.status_code, 400)
        payload = json.loads(response.content)
        self.assertEqual(payload["messages"], ["invalid transition"])
