import unittest
import companiesHandler

class Test_test_newCompanyForm(unittest.TestCase):
    def test_newCompanyTitle(self):
        self.assertFalse(companiesHandler.testFormTitle())

    def test_newCompanyDescription(self):
        self.assertFalse(companiesHandler.testFormDescription())

if __name__ == '__main__':
    unittest.main()
