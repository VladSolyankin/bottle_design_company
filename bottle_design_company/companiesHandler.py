from operator import contains
import os
from bottle import post, request, datetime, template
import re
import string


# Function for new company form validation
@post('/companies', method='post')
def companiesHandler():
    # Receiving form data
    companyTitle = request.forms.get("TITLE")
    companyDescription = request.forms.get("DESCRIPTION")
    companyPhone = request.forms.get("PHONE")
    companyImage = request.files.get("IMAGE")

    # Checking for filling all input fields
    if not len(companyTitle) or not len(companyDescription) or not len(companyPhone):
        return template('companies.tpl', error='Fill all the fields!')
    
    # Saving loaded images in folder
    start_path = f"./static/companyImages/{companyImage.filename}"
    if not os.path.exists(start_path):
        companyImage.save(start_path)
    else:
        # Returns template with error
        return template('companies.tpl', error='Company already exists!')

    # Writing data about new company in text file
    with open('companies.txt', 'a') as f:
        f.write(f"\n./static/companyImages/{companyImage.filename}:{companyTitle}:{companyDescription}:{companyPhone}")

    # Returns updated template
    return template('companies.tpl', error='')  



# Function for new company title test
def testFormTitle(newCompanyTitleList):
    result = []
    regex = re.compile(r'[A-Za-z]+')
    for i in newCompanyTitleList:
        # False if title too short, number-only or doesn't match regex-pattern
        if len(i) < 2 or i.isnumeric() or not re.fullmatch(regex, i):
            result.append(False)
        else:
            result.append(True)
    return result        


# Function for new company description test
def testFormDescription(newCompanyDescriptionList):
    result = []
    regex = re.compile(r'([A-Za-z]+\s)([0-9!@#$%^&*()]*)')
    for i in newCompanyDescriptionList:
        # False if title too short or number-only
        if len(i) < 10 or i.isnumeric() or not re.match(regex, i):
            result.append(False)
        else:
            result.append(True)
    return result

# Function for new company phone
def testFormPhone(newCompanyPhoneList):
    regex = re.compile(r'8-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}')
    result = []

    for i in newCompanyPhoneList:
        # False if phone isn't matching regex-pattern
        if not re.fullmatch(regex, i):
            result.append(False)
        else:
            result.append(True)

    return result