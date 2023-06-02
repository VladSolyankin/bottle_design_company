import unittest
import companiesHandler

class Test_test_addNewCompany_data2(unittest.TestCase):
    def test_newCompanyTitle(self):
        #arrange
        inputValues = ["Mastercard", "Mitsubishu", "McDonalds", "CompanyName", "HelloWorld"]
        expectedValues = [True for i in range(len(inputValues))]
        #act
        receivedValues = companiesHandler.testFormTitle(inputValues)
        #assert
        self.assertEqual(expectedValues, receivedValues)

    def test_newCompanyDescription(self):
        #arrange
        inputValues = ["Normal company description", "Description with !@#$^&*", "Description with 123456"]
        expectedValues = [True for i in range(len(inputValues))]
        #act
        receivedValues = companiesHandler.testFormDescription(inputValues)
        #assert
        self.assertEqual(expectedValues, receivedValues)

    def test_newCompanyPhone(self):
        #arrange
        inputValues = ["8-921-994-42-83", "8-912-812-22-01", "8-912-812-22-01", "8-999-888-77-66", "8-812-412-12-44"]
        expectedValues = [True for i in range(len(inputValues))]
        #act
        receivedValues = companiesHandler.testFormPhone(inputValues)
        #assert
        self.assertEqual(expectedValues, receivedValues)

if __name__ == '__main__':
    unittest.main()
