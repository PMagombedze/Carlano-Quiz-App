"""
views
"""

from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route('/')
@views.route('/home')
def home():
    """home template"""
    return render_template('index.html')

@views.route('/python')
def func():
    return render_template('quizzes/python.html')