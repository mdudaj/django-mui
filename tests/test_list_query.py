import unittest
from unittest.mock import Mock

from django_mui.list_query import get_ordering_from_request, get_page_size_from_request
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

    def test_get_page_size_from_request_falls_back_to_default_for_invalid_value(self):
        request = Mock(GET={"page_size": "big"})

        page_size = get_page_size_from_request(request, [2, 10, 25], 2)

        self.assertEqual(page_size, 2)

    def test_get_page_size_from_request_falls_back_to_default_for_unbounded_value(self):
        request = Mock(GET={"page_size": "1000"})

        page_size = get_page_size_from_request(request, [2, 10, 25], 2)

        self.assertEqual(page_size, 2)

    def test_list_query_preserves_valid_page_size_for_pagination(self):
        request = Mock(GET={"q": "orders", "ordering": "-created_at", "page_size": "25"})

        query = list_query({"request": request}, 2)

        self.assertEqual(query, "q=orders&ordering=-created_at&page_size=25&page=2")

    def test_list_query_ignores_invalid_page_size_for_pagination(self):
        request = Mock(GET={"q": "orders", "ordering": "-created_at", "page_size": "0"})

        query = list_query({"request": request}, 2)

        self.assertEqual(query, "q=orders&ordering=-created_at&page=2")


if __name__ == "__main__":
    unittest.main()
