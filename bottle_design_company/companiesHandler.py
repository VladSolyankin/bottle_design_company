from operator import contains
from bottle import post, request, datetime, template


@post('/companies', method='post')
def companiesHandler():
    companyTitle = request.forms.get("TITLE")
    companyDescription = request.forms.get("DESCRIPTION")
    companyPhone = request.forms.get("PHONE")
    companyImage = request.files.get("IMAGE")
        
    companyImage.save(f"C:/Users/79117/source/repos/bottle_design_company/bottle_design_company/static/companyImages/{companyImage.filename}")

    with open('companies.txt', 'a') as f:
        f.write(f"\n./static/companyImages/{companyImage.filename}:{companyTitle}:{companyDescription}:{companyPhone}")

    return template('companies.tpl', error='')