"""
Routes and views for the bottle application.
"""
import re
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

