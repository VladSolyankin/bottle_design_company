from operator import contains
import os
from bottle import post, request, datetime, template


@post('/companies', method='post')
def companiesHandler():
    # Receiving form data
    companyTitle = request.forms.get("TITLE")
    companyDescription = request.forms.get("DESCRIPTION")
    companyPhone = request.forms.get("PHONE")
    companyImage = request.files.get("IMAGE")
    
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



def testFormTitle():
    # Receiving form data
    companyTitle = request.forms.get("TITLE")

    if len(companyTitle) < 2 or not companyTitle[0].isupper():
         return False

    return True
   

def testFormDescription():
    companyDescription = request.forms.get("DESCRIPTION")

    if len(companyDescription) < 10:
        return False

    return True