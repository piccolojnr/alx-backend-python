#!/usr/bin/env python3
"""
Test client module.
"""
import unittest
from unittest.mock import PropertyMock, patch, Mock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Test GithubOrgClient class.
    """

    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    def test_org(self, org_name):
        """
        Test GithubOrgClient.org.
        """
        with patch("client.get_json") as mock_get_json:
            mock_get_json.return_value = {"login": org_name}
            test = GithubOrgClient(org_name)
            self.assertEqual(test.org, {"login": org_name})
            self.assertEqual(test.org, {"login": org_name})
            mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """
        Test GithubOrgClient._public_repos_url.
        """
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {"repos_url": "http://google.com"}
            test = GithubOrgClient("google")
            self.assertEqual(test._public_repos_url, "http://google.com")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test GithubOrgClient.public_repos.
        """
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "my_license"}}
        ]

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = "http://google.com"

            test = GithubOrgClient("google")
            self.assertEqual(test.public_repos(), ["repo1"])

            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand(
        [
            [{"license": {"key": "my_license"}}, "my_license", True],
            [{"license": {"key": "other_license"}}, "my_license", False],
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """
        Test GithubOrgClient.has_license.
        """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected,
        )


@parameterized_class(
    [
        {
            "org_payload": TEST_PAYLOAD[0][0],
            "repos_payload": TEST_PAYLOAD[0][1],
            "expected_repos": TEST_PAYLOAD[0][2],
            "apache2_repos": TEST_PAYLOAD[0][3],
        }
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Test GithubOrgClient class.
    """

    @classmethod
    def setUp(cls) -> None:
        """
        Set up test.
        """

        def get_effect(url):
            """
            Get effect.
            """
            if url == "https://api.github.com/orgs/google":
                return Mock(**{"json.return_value": cls.org_payload})
            return Mock(**{"json.return_value": cls.repos_payload})

        cls.get_patcher = patch("requests.get", side_effect=get_effect)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDown(cls) -> None:
        """
        Tear down test.
        """
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
