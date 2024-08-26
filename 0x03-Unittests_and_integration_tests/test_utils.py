#!/usr/bin/env python3
"""
    Using Mock, Parameterize and patch to test functions, methods and classes.
"""
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """ Define test methods access_nested_map(). """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, result: Any) -> None:
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
    """ Tests the get_json funtion """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url: str, payload: Dict,
                      mock_get: Mock) -> None:
        """ Test the get_json function without making http call. """
        # Create a Mock responce object with a json method
        mock_res = Mock()
        mock_res.json.return_value = payload
        # Set the mock get method to return the mock reponse
        mock_get.return_value = mock_res

        result = get_json(url)
        mock_get.assert_called_once_with(url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """ Defines a test the memoize decorator in utils module. """
    def test_memoize(self) -> None:
        """ Test that the memoize decorator caches the result. """
        class TestClass:
            """ Defines a method that uses the memoize decorator. """
            def a_method(self) -> int:
                """ Returns 42. """
                return 42

            @memoize
            def a_property(self) -> int:
                """ Returns the return value of a_method. """
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method',
                          return_value=42) as mock_method:
            test_result1 = test_obj.a_property
            test_result2 = test_obj.a_property

            self.assertEqual(test_result1, 42)
            self.assertEqual(test_result2, 42)

            mock_method.assert_called_once()
