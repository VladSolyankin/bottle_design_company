
import unittest
import articlesHandler

class ValidateURL(unittest.TestCase):
    def test_valid_URLS(self):
        #act
        urls = ["https://google.com", "https://yandex.ru", 
                "https://drom.ru", "https://youtube.com", "https://github.com"]
        #arrange
        #assert
        for i in range(len(urls)):
            self.assertTrue(articlesHandler.regex_url(urls[i]))
    def test_invalid_URLS(self):
        #act
        urls = ["234", "www.google.com", "asdfasdfasdf.vom", "https://@#$",
               "https:/google.com", "https://google,com", "https://google.%@"]
        #arrange
        #assert
        for i in range(len(urls)):
            self.assertFalse(articlesHandler.regex_url(urls[i]))
