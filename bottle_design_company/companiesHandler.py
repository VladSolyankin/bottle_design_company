from operator import contains
import os
from bottle import post, request, datetime, template


@post('/companies', method='post')
def companiesHandler():
    companyTitle = request.forms.get("TITLE")
    companyDescription = request.forms.get("DESCRIPTION")
    companyPhone = request.forms.get("PHONE")
    companyImage = request.files.get("IMAGE")
    
    start_path = f"./static/companyImages/{companyImage.filename}"
    if not os.path.exists(start_path):
        companyImage.save(start_path)
    else:
        return template('companies.tpl', error='Company already exists!')

    with open('companies.txt', 'a') as f:
        f.write(f"\n./static/companyImages/{companyImage.filename}:{companyTitle}:{companyDescription}:{companyPhone}")

    return template('companies.tpl', error='')