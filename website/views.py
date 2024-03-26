"""
views
"""

from flask import Blueprint, render_template, make_response, request
from htmlmin import minify
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route('/')
@views.route('/home')
def home():
    """home template"""
    html = render_template('index.html')
    minified_html = minify(html)
    response = make_response(minified_html)
    response.headers['Content-Disposition'] = 'inline'

    return response


@views.route('/python')
def func():
    html = render_template('quizzes/python.html')
    minified_html = minify(html)
    response = make_response(minified_html)
    response.headers['Content-Disposition'] = 'inline'

    return response


@views.route('/quiz/dashboard')
@login_required
def dashboard():
    referrer = request.referrer

    if referrer.endswith('/auth/Login.action'):
        return render_template('quizzes/dashboard.html', user=current_user)
    elif referrer.endswith('/quiz/quizzes/python'):
        return "quizzes"
    else:
        return render_template('quizzes/dash_.html', user=current_user)
