import re
from genericpath import exists
from bottle import template
from bottle import route, view, post, request
from datetime import datetime

@post("/articles")
def add_article():

   

    name = request.forms.get("name")
    desc = request.forms.get("desc")
    image = request.files.get("img")
    src_link = request.forms.get("src-link")
    author = request.forms.get("author")


    path = "C:/Users/admin/source/repos/bottle_design_company/bottle_design_company/static/images/articles/" + image.filename



    error = ""
    if (name == ""):
        error += "Name was empty; "
    if (desc == ""):
        error += "Desc was empty; "
    if (src_link == ""):
        error += "Source link was empty; "

    
    
    if (author == ""):
        error += "Author was empty; "
    if (image.filename == "empty"):
        error += "Filename was empty; "
    elif (not image.filename.split('.')[-1] in ["png", "jpg"]):
        error += "File was wrong format (must be .png or .jpg) "

    if (error != ""):
        return template("articles.tpl", error = error)
    if (not exists(path)):
        image.save(path)
    else:
         return template("articles.tpl", error = "This files is already exists on the server")
     
    
    

    with open("C:/Users/admin/source/repos/bottle_design_company/bottle_design_company/static/articles.txt", "a") as f:
        f.write(f"{name}~../static/images/articles/{image.filename}~{desc}~{src_link}~{author}~{datetime.now().year}.{datetime.now().month}.{datetime.now().day}\n");
        return template("articles.tpl", error = "Your article was added, refresh page to see changes")

def validate_url(url):
    formaturl = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
    return bool(re.fullmatch(re.compile(formaturl), url))