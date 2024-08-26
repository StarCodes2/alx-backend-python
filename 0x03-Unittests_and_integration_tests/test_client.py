#!/usr/bin/env python3
"""
    Using Mock, Parameterize and patch to test functions, methods and classes.
"""
import unittest
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
from typing import Dict


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


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ """
    @classmethod
    def setUpClass(cls):
        """Set up class-wide mocks before any test in this class runs."""
        def get_side_effect(url):
            """ Side effect function for requests.get().json() """
            if url == "https://api.github.com/orgs/google":
                return MagicMock(json=lambda: cls.org_payload)
            return MagicMock(json=lambda: cls.repos_payload)

        cls.get_patcher = patch('requests.get', side_effect=get_side_effect)
        cls.mock_get = cls.get_patcher.start()

    def test_public_repos(self):
        """ Test for the public_repos method. """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("XLICENSE"), [])
        self.mock_get.assert_called()

    def test_public_repos_with_license(self):
        """ Test the public_repos method with license filtering. """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("XLICENSE"), [])
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
        self.mock_get.assert_called()

    @classmethod
    def tearDownClass(cls):
        """ Tears down class-wide mocks after all tests in this class run. """
        cls.get_patcher.stop()
