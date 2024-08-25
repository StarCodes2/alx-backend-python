#!/usr/bin/env python3
"""
    Using Mock, Parameterize and patch to yesy functions, methods and classes.
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Any, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """ Define test methods access_nested_map(). """
    @parameterized.expand([
        ("Single item in map and path", {"a": 1}, ("a",), 1),
        ("Nested map/single key", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("Nexted map/two keys", {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, name: str, nested_map: Mapping[str, Any],
                               path: Sequence[str], result: Any) -> None:
        """ Tests the access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), result)


class TestGetJson(unittest.TestCase):
    """ """
    pass
