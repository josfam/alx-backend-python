#!/usr/bin/env python3

"""Test cases for the access_nested_map function from utils file"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Tests whether access_nested_map works as expected"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests functionality of utils.get_json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mocked_get):
        # mock response object, and json content
        mock_response_obj = mocked_get.return_value
        mock_response_obj.json.return_value = test_payload

        # call the function to test
        result = get_json(test_url)

        # assertions
        mocked_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
