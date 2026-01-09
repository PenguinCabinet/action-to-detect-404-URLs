from main import *
import unittest

class TestMain(unittest.TestCase):
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
            search_and_filter_urls_directory("./test","allow","2..",True,1),
            [
                {
                    'status_code': 404,
                    'url': 'http://example.com/404_TEST_TEST'
                },
                {
                    'status_code': -1,
                    'url': 'http://example.example'
                },
            ]
        )

if __name__ == '__main__':
    unittest.main()