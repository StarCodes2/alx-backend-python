#!/usr/bin/env python3
"""
    Using Mock, Parameterize and patch to test functions, methods and classes.
"""
import unittest
from unittest.mock import Mock, PropertyMock, patch
from client import GithubOrgClient
from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence


class TestGithubOrgClient(unittest.TestCase):
    """ Defines tests for class GithubOrgClient. """
    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True}),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, payload: Dict, mock_get: Mock) -> None:
        """
            Test that the org property returns the correct result without
            an external http call.
        """
        mock_get.return_value = payload
        test_obj = GithubOrgClient(org)
        self.assertEqual(test_obj.org, payload)

        expected_url = test_obj.ORG_URL.format(org=org)
        mock_get.assert_called_with(expected_url)

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    def test_public_repos_url(self, org: str) -> None:
        """ Mock a property to test its return value. """
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as org_mock:
            payload = {
                "repos_url": GithubOrgClient.ORG_URL.format(org=org)
            }
            org_mock.return_value = payload
            test_obj = GithubOrgClient(org)
            self.assertEqual(test_obj._public_repos_url, payload["repos_url"])
