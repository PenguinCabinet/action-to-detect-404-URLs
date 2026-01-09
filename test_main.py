from main import *
import unittest

unittest.util._MAX_LENGTH = 10**7

class TestMain(unittest.TestCase):
    maxDiff = None
    def test_search_urls(self):
        self.assertEqual(
            search_urls("https://example.com example.com https://example.com"),
            [
                "https://example.com",
                "https://example.com",
            ]
        )

    def test_search_and_filter_urls_directory(self):
        self.assertEqual(
            search_and_filter_urls_directory("./test","allow","2..",False,1),
            [
                {
                    'status_code': 404,
                    'url': 'http://example.com/404_TEST_TEST'
                }
            ]
        )
        self.assertEqual(
            sorted(
                search_and_filter_urls_directory("./test","allow","2..",True,1),
                key=lambda v:v["url"]
            ),
            sorted([
                {
                    'status_code': 404,
                    'url': 'http://example.com/404_TEST_TEST'
                },
                {
                    'status_code': -1,
                    'url': 'http://example.example'
                },
            ],key=lambda v:v["url"])
        )
        self.assertEqual(
            sorted(
                search_and_filter_urls_directory("./test","deny","4..",False,1),
                key=lambda v:v["url"]
            ),
            sorted([
                {
                    'status_code': 404,
                    'url': 'http://example.com/404_TEST_TEST'
                },
            ],key=lambda v:v["url"])
        )

if __name__ == '__main__':
    unittest.main()