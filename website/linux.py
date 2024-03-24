"""
linux quiz
"""

from flask import Blueprint, render_template, make_response
from htmlmin import minify
from flask_login import login_required, current_user

linux = Blueprint("linux", __name__)

@linux.route('/')
@login_required
def quiz():
    return render_template('quizzes/linux.html')
