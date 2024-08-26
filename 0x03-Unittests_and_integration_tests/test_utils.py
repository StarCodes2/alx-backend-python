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
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping[str, Any],
                               path: Sequence[str], result: Any) -> None:
        """ Tests the access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, result: str) -> None:
        """ Test for KeyError excecptions. """
        with self.assertRaises(KeyError) as ke:
            value = access_nested_map(nested_map, path)
        self.assertEqual(str(ke.exception), result)


class TestGetJson(unittest.TestCase):
    """ """
    pass
