"""
Routes and views for the bottle application.
"""

from genericpath import exists
from bottle import template
from bottle import route, view, post, request
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contacts')
@view('contacts')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/portfolio')
@view('portfolio')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year,
        
    )

@route('/companies')
@view('companies')
def about():
    """Renders the about page."""
    return dict(
        error=''
    )

@route('/articles')
@view('articles')
def articles():
    """Renders the about page."""
    return dict(
        error = ""
    )

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
    if (error != ""):
        return template("articles.tpl", error = error)
    if (not exists(path)):
        image.save(path)
    else:
         return template("articles.tpl", error = "This files is already exists on the server")
    
    with open("C:/Users/admin/source/repos/bottle_design_company/bottle_design_company/static/articles.txt", "a") as f:
        f.write(f"{name}~../static/images/articles/{image.filename}~{desc}~{src_link}~{author}~{datetime.now().year}.{datetime.now().month}.{datetime.now().day}\n");
        return template("articles.tpl", error = "Your article was added, refresh page to see changes")
