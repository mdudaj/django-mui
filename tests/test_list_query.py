import unittest
from unittest.mock import Mock

from django_mui.list_query import get_ordering_from_request
from django_mui.templatetags.django_mui_list import list_query


class ListQueryTests(unittest.TestCase):
    def test_get_ordering_from_request_falls_back_to_default_for_invalid_value(self):
        request = Mock(GET={"ordering": "unknown"})

        ordering = get_ordering_from_request(request, ["name", "-name"], "name")

        self.assertEqual(ordering, "name")

    def test_list_query_preserves_q_and_ordering_for_pagination(self):
        request = Mock(GET={"q": "orders", "ordering": "-created_at"})

        query = list_query({"request": request}, 2)

        self.assertEqual(query, "q=orders&ordering=-created_at&page=2")


if __name__ == "__main__":
    unittest.main()
