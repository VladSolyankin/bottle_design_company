
import unittest
import articlesHandler

class SimpleFields(unittest.TestCase):
    def test_valid_name(self):
        #act
        names = ["General discussion", "How to cook eggs",
                "Design methods", "Magical animations, Give it a break"]
        #arrange
        error = ""
        for i in range(len(names)):
            error += articlesHandler.validate_name(names[i])
            if (error != ""):
                break
        #assert
        self.assertEqual("", error)
    def test_invalid_name(self):
        #act
        names = ["", "1", "A", "B"]
        #arrange
        error = ""
        for i in range(len(names)):
            error += articlesHandler.validate_name(names[i])
            if (error != ""):
                break
        #assert
        self.assertNotEqual("", error)
    
    def test_valid_desc(self):
        #act
        descs = ["Some description", "HOHOHO", "Nice desc", "Description"]
        #arrange
        error = ""
        for i in range(len(descs)):
            error += articlesHandler.validate_desc(descs[i])
            if (error != ""):
                break
        #assert
        self.assertEqual("", error)
    def test_invalid_desc(self):
        #act
        descs = ["", "texttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttext"]
        #arrange
        error = ""
        for i in range(len(descs)):
            error += articlesHandler.validate_desc(descs[i])
            if (error != ""):
                break
        #assert
        self.assertNotEqual("", error)
    def test_valid_author(self):
        authors = ["author", "someauthor", "test"]
        #arrange
        error = ""
        for i in range(len(authors)):
            error += articlesHandler.validate_desc(authors[i])
            if (error != ""):
                break
        #assert
        self.assertEqual("", error)
    def test_invalid_author(self):
        authors = ["", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"]
        #arrange
        error = ""
        for i in range(len(authors)):
            error += articlesHandler.validate_desc(authors[i])
            if (error != ""):
                break
        #assert
        self.assertNotEqual("", error)
        
       