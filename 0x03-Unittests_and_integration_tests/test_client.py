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

    @parameterized.expand([
        ("google", [{"name": "Search Repo"}]),
        ("abc", [{"name": "abc Repo"}]),
    ])
    @patch('client.get_json')
    def test_public_repos(self, org: str, payload: Dict,
                          mock_get: Mock) -> None:
        """ Mocks two properties to test the return value of one. """
        mock_get.return_value = payload
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as repos_mock:
            url = GithubOrgClient.ORG_URL.format(org=org)
            repos_mock.return_value = url

            test_obj = GithubOrgClient(org)
            payload_list = [pay['name'] for pay in payload]
            self.assertEqual(test_obj.public_repos(), payload_list)

            repos_mock.assert_called_once()

        mock_get.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         license_key: str, expected: bool) -> None:
        """ Tests the has_license method. """
        test_bool = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(test_bool, expected)
