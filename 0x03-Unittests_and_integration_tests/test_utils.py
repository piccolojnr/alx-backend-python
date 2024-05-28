#!/usr/bin/env python3
"""Generic utilities for github org client."""
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Test access_nested_map function.
    """

    @parameterized.expand(
        [
            [{"a": 1}, ("a",), 1],
            [{"a": {"b": 2}}, ("a",), {"b": 2}],
            [{"a": {"b": 2}}, ("a", "b"), 2],
        ]
    )
    def test_access_nested_map(self, nested_map, path, value):
        """Test access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), value)

    @parameterized.expand(
        [
            [{}, ("a",)],
            [{"a": 1}, ("a", "b")],
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map function."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test get_json function.
    """

    @parameterized.expand(
        [
            ["http://example.com", {"payload": True}],
            ["http://holberton.io", {"payload": False}],
        ]
    )
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json function."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Test memoize decorator."""

    def test_memoize(self):
        """Test memoize."""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_method:
            mock_method.return_value = 42

            test_obj = TestClass()
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
