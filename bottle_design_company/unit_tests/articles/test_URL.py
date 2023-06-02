
import unittest
import articlesHandler

class ValidateURL(unittest.TestCase):
    def test_valid_URLS(self):
        urls = ["https://google.com", "https://yandex.ru", "https://drom.ru"]
        for i in range(len(urls)):
            self.assertTrue(articlesHandler.validate_url(urls[i]))
    def test_invalid_URLS(self):
        urls = ["234", "www.google.com", "asdfasdfasdf.vom", "https://@#$",
               "https:/google.com", "https://google,com", "https://google.%@"]
        for i in range(len(urls)):
            self.assertFalse(articlesHandler.validate_url(urls[i]))