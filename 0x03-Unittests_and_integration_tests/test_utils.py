#!/usr/bin/env python3
"""
    Using Mock, Parameterize and patch to yesy functions, methods and classes.
"""
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json
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
