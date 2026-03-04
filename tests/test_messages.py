import unittest

from django.contrib.messages import constants as message_constants
from django.contrib.messages.storage.base import Message

from django_mui.messages import get_snackbar_messages_payload


class SnackbarMessagesPayloadTests(unittest.TestCase):
    def test_maps_level_and_message_text(self):
        messages = [
            Message(message_constants.SUCCESS, "Done"),
            Message(message_constants.WARNING, "Check input"),
            Message(message_constants.ERROR, "Failed"),
        ]

        payload = get_snackbar_messages_payload(messages)

        self.assertEqual(
            payload,
            [
                {"level": "success", "severity": "success", "message": "Done"},
                {"level": "warning", "severity": "warning", "message": "Check input"},
                {"level": "error", "severity": "error", "message": "Failed"},
            ],
        )

    def test_defaults_unknown_levels_to_info(self):
        payload = get_snackbar_messages_payload([Message(0, "Heads up")])

        self.assertEqual(
            payload,
            [{"level": "info", "severity": "info", "message": "Heads up"}],
        )


if __name__ == "__main__":
    unittest.main()
