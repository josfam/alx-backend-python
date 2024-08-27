#!/usr/bin/env python3

"""Test cases for client methods"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([('google',), ('abc',)])
    @patch('client.get_json', return_value={'key': 'value'})
    def test_org(self, org_name, mock_get_json):
        # instantiate this org
        client = GithubOrgClient(org_name)
        # call the org method
        result = client.org
        self.assertEqual(result, {'key': 'value'})

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
