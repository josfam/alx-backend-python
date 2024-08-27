#!/usr/bin/env python3

"""Test cases for client methods"""

import unittest
from unittest.mock import patch, PropertyMock
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

    @patch(
        'client.GithubOrgClient._public_repos_url', new_callable=PropertyMock
    )
    def test_public_repos_url(self, mock_public_repos_url):
        placeholder_url = 'https://api.github.com/orgs/place_holder/repos'

        mock_public_repos_url.return_value = placeholder_url

        client = GithubOrgClient('placeholder_org')
        result = client._public_repos_url
        self.assertEqual(result, placeholder_url)
