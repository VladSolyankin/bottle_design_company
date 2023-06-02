import unittest
import companiesHandler

class Test_test_newCompanyForm(unittest.TestCase):
    def test_newCompanyTitle(self):
        #arrange
        inputValues = ["", "1234567890", "!@#$%^&*()", "X", "_.,", "abc!@#", "123asd!@#"]
        expectedValues = [False for i in range(len(inputValues))]
        #act
        receivedValues = companiesHandler.testFormTitle(inputValues)
        #assert
        self.assertEqual(expectedValues, receivedValues)

    def test_newCompanyDescription(self):
        #arrange
        inputValues = ["", "Too short", "!@#$%^&*()", "1234567890", "_.,", "abc!@#", "123asd!@#"]
        expectedValues = [False for i in range(len(inputValues))]
        #act
        receivedValues = companiesHandler.testFormDescription(inputValues)
        #assert
        self.assertEqual(expectedValues, receivedValues)

    def test_newCompanyPhone(self):
        #arrange
        inputValues = ["8(999)-999-99-99", "89998887766", "8-99-99-99-99-11", "!@#$%^&*()", "", "09123412312", "VladSolyankin"]
        expectedValues = [False for i in range(len(inputValues))]
        #act
        receivedValues = companiesHandler.testFormPhone(inputValues)
        #assert
        self.assertEqual(expectedValues, receivedValues)

if __name__ == '__main__':
    unittest.main()
