import unittest
from unittest.mock import Mock

from django_mui.list_query import (
    get_filters_from_request,
    get_ordering_from_request,
    get_page_size_from_request,
    resolve_filters,
)
from django_mui.templatetags.django_mui_list import list_index, list_query


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

    def test_list_query_ignores_unbounded_page_size_for_pagination(self):
        request = Mock(GET={"q": "orders", "ordering": "-created_at", "page_size": "1000"})

        query = list_query({"request": request}, 2)

        self.assertEqual(query, "q=orders&ordering=-created_at&page=2")

    def test_list_query_rejects_page_size_not_in_allowed_list(self):
        request = Mock(GET={"q": "orders", "ordering": "-created_at", "page_size": "1000"})

        query = list_query({"request": request, "allowed_page_sizes": [2, 10, 25]}, 2)

        self.assertEqual(query, "q=orders&ordering=-created_at&page=2")

    def test_list_query_preserves_page_size_in_allowed_list(self):
        request = Mock(GET={"q": "orders", "ordering": "-created_at", "page_size": "10"})

        query = list_query({"request": request, "allowed_page_sizes": [2, 10, 25]}, 2)

        self.assertEqual(query, "q=orders&ordering=-created_at&page_size=10&page=2")

    def test_resolve_filters_keeps_valid_values(self):
        raw = {"status": "active", "region": "eu"}
        allowed = {"status": ["active", "inactive"], "region": ["eu", "us"]}

        result = resolve_filters(raw, allowed)

        self.assertEqual(result, {"status": "active", "region": "eu"})

    def test_resolve_filters_drops_invalid_values(self):
        raw = {"status": "deleted", "region": "eu"}
        allowed = {"status": ["active", "inactive"], "region": ["eu", "us"]}

        result = resolve_filters(raw, allowed)

        self.assertEqual(result, {"region": "eu"})

    def test_resolve_filters_falls_back_to_defaults(self):
        raw = {"status": "deleted"}
        allowed = {"status": ["active", "inactive"], "region": ["eu", "us"]}
        defaults = {"status": "active"}

        result = resolve_filters(raw, allowed, defaults)

        self.assertEqual(result, {"status": "active"})

    def test_resolve_filters_omits_missing_without_default(self):
        raw = {}
        allowed = {"status": ["active", "inactive"]}

        result = resolve_filters(raw, allowed)

        self.assertEqual(result, {})

    def test_get_filters_from_request_extracts_valid_filters(self):
        request = Mock(GET={"status": "active", "region": "eu", "q": "test"})
        allowed = {"status": ["active", "inactive"], "region": ["eu", "us"]}

        result = get_filters_from_request(request, allowed)

        self.assertEqual(result, {"status": "active", "region": "eu"})

    def test_get_filters_from_request_ignores_empty_and_invalid(self):
        request = Mock(GET={"status": "", "region": "invalid"})
        allowed = {"status": ["active", "inactive"], "region": ["eu", "us"]}

        result = get_filters_from_request(request, allowed)

        self.assertEqual(result, {})

    def test_list_query_preserves_multiple_filter_params(self):
        request = Mock(GET={"q": "orders", "ordering": "-created_at", "status": "active", "region": "eu"})
        allowed_filters = {"status": ["active", "inactive"], "region": ["eu", "us"]}

        query = list_query({"request": request, "allowed_filters": allowed_filters}, 2)

        self.assertEqual(query, "q=orders&ordering=-created_at&status=active&region=eu&page=2")

    def test_list_query_drops_invalid_filter_params(self):
        request = Mock(GET={"q": "orders", "status": "deleted", "region": "eu"})
        allowed_filters = {"status": ["active", "inactive"], "region": ["eu", "us"]}

        query = list_query({"request": request, "allowed_filters": allowed_filters}, 2)

        self.assertEqual(query, "q=orders&region=eu&page=2")

    def test_list_query_filters_survive_with_page_size(self):
        request = Mock(GET={"status": "active", "page_size": "25"})
        allowed_filters = {"status": ["active", "inactive"]}

        query = list_query({"request": request, "allowed_filters": allowed_filters}, 3)

        self.assertEqual(query, "page_size=25&status=active&page=3")

    def test_list_index_returns_item_for_valid_index(self):
        self.assertEqual(list_index(["Order", "Customer"], 1), "Customer")

    def test_list_index_returns_none_for_invalid_inputs(self):
        self.assertIsNone(list_index(["Order"], "abc"))
        self.assertIsNone(list_index(["Order"], 2))
        self.assertIsNone(list_index("Order", 0))


if __name__ == "__main__":
    unittest.main()
