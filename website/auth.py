"""
Authentication
"""

# primary key use uuid.uuid4()
from flask import render_template, redirect, url_for, request, Blueprint
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

auth = Blueprint("auth", __name__)


@auth.route('auth/Login.action', strict_slashes=False)
def login():
    """home template"""
    return render_template('auth/login.html', strict_slashes=False)

@auth.route('auth/Registration.action')
def signup():
    """home template"""
    return render_template('auth/signup.html')
