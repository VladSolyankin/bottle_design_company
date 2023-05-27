"""
Routes and views for the bottle application.
"""

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
        year=datetime.now().year
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
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@post("/articles")
def add_article():
    name = request.forms.get("name")
    desc = request.forms.get("desc")
    image = request.files.get("img")
    author = request.forms.get("author")

    path = "C:/Users/admin/source/repos/bottle_design_company/bottle_design_company/static/images/articles/" + image.filename

    image.save(path)

    with open("C:/Users/admin/source/repos/bottle_design_company/bottle_design_company/static/articles.txt", "a") as f:
        f.write(f"\n{name}~../static/images/articles/{image.filename}~{desc}~{author}~{datetime.now().year}");