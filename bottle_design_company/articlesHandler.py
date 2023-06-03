import re
from genericpath import exists
from bottle import template
from bottle import route, view, post, request
from datetime import datetime

@post("/articles")
def add_article():

   
    #get all data from the form
    name = request.forms.get("name")
    desc = request.forms.get("desc")
    image = request.files.get("img")
    src_link = request.forms.get("src-link")
    author = request.forms.get("author")

    path = "C:/Users/admin/source/repos/bottle_design_company/bottle_design_company/static/images/articles/" + image.filename
    

    #validate all data
    error = ""
    error += validate_name(name)
    error += validate_desc(desc)
    error += validate_img(path, image)
    error += validate_author(author)
    error += validate_url(src_link)

    #two ways of return

    #with a error if it is not empty
    if (error != ""):
        
        return template("articles.tpl", error = error)

    #or successful
    image.save(path)
    with open("C:/Users/admin/source/repos/bottle_design_company/bottle_design_company/static/articles.txt", "a") as f:
        f.write(f"{name}~../static/images/articles/{image.filename}~{desc}~{src_link}~{author}~{datetime.now().year}.{datetime.now().month}.{datetime.now().day}\n");
        return template("articles.tpl", error = "Your article was added, refresh page to see changes")

def regex_url(url): #regex for link
    formaturl = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
    return bool(re.fullmatch(re.compile(formaturl), url))
def validate_url(url): #checkin link for a valid format
    if (not regex_url(url)):
        return "Link was wrong format; "
    return ""

def validate_name(name): #checking name for a valid format
    if (name == ""):
        return "Name was empty; "
    if (len(name) < 5):
        return "Name was too small (must be 5 symbols at least); "
    if (len(name) > 50):
        return "Name was too long; "
    return ""

def validate_desc(desc): #checking desc for a valid format
    if (desc == ""):
        return "Desc was empty; "
    if (len(desc) > 300):
        return "Desc was too long; "
    return ""

def validate_author(author): #checking author for a valid format
    if (author == ""):
        return "Author was empty;  "
    if (len(author) > 30):
        return "Author was too long; "
    return ""

def validate_img(path, image): #checking img for a valid format

    
    if image.filename == "empty":
        return "Image was not loaded; "
    if (exists(path)):
        return "That image is already on server (choose another name); "
    return ""