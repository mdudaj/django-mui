import unittest
from unittest.mock import Mock, patch

from django.urls import NoReverseMatch

from django_mui.navigation import _resolve_url, build_navigation


class NavigationTests(unittest.TestCase):
    def test_build_navigation_excludes_items_without_required_permissions(self):
        user = Mock(has_perms=Mock(return_value=False))
        request = Mock(user=user, resolver_match=Mock(view_name=None))
        registry = [
            {
                "id": "admin",
                "label": "Admin",
                "route_name": "admin:index",
                "required_permissions": ["admin.view_site"],
            }
        ]

        with patch("django_mui.navigation.reverse", return_value="/resolved/"):
            navigation = build_navigation(request, registry=registry)

        self.assertEqual(navigation, [])
        user.has_perms.assert_called_once_with(["admin.view_site"])

    def test_build_navigation_marks_parent_active_when_child_route_matches(self):
        user = Mock(has_perms=Mock(return_value=True))
        request = Mock(user=user, resolver_match=Mock(view_name="orders:detail"))
        registry = [
            {
                "id": "orders",
                "label": "Orders",
                "route_name": "orders:list",
                "children": [
                    {
                        "id": "order-detail",
                        "label": "Order Detail",
                        "route_name": "orders:detail",
                        "required_permissions": [],
                    }
                ],
                "required_permissions": [],
            }
        ]

        with patch("django_mui.navigation.reverse", return_value="/resolved/"):
            navigation = build_navigation(request, registry=registry)

        self.assertTrue(navigation[0]["children"][0]["active"])
        self.assertTrue(navigation[0]["active"])

    def test_build_navigation_filters_children_by_permissions(self):
        user = Mock(has_perms=Mock(side_effect=[True, False]))
        request = Mock(user=user, resolver_match=Mock(view_name=None))
        registry = [
            {
                "id": "parent",
                "label": "Parent",
                "route_name": "parent:list",
                "required_permissions": ["parent.view"],
                "children": [
                    {
                        "id": "child",
                        "label": "Child",
                        "route_name": "child:list",
                        "required_permissions": ["child.view"],
                    }
                ],
            }
        ]

        with patch("django_mui.navigation.reverse", return_value="/resolved/"):
            navigation = build_navigation(request, registry=registry)

        self.assertEqual(len(navigation), 1)
        self.assertEqual(navigation[0]["children"], [])

    def test_build_navigation_marks_item_active_for_matching_route_prefix(self):
        user = Mock(has_perms=Mock(return_value=True))
        request = Mock(user=user, resolver_match=Mock(view_name="orders:detail"))
        registry = [
            {
                "id": "orders",
                "label": "Orders",
                "route_name": "orders:list",
                "active_view_prefixes": ["orders:"],
                "required_permissions": [],
            }
        ]

        with patch("django_mui.navigation.reverse", return_value="/resolved/"):
            navigation = build_navigation(request, registry=registry)

        self.assertTrue(navigation[0]["active"])

    def test_resolve_url_returns_fallback_for_unresolvable_route(self):
        with patch("django_mui.navigation.reverse", side_effect=NoReverseMatch):
            self.assertEqual(_resolve_url("missing:view"), "#")


if __name__ == "__main__":
    unittest.main()
