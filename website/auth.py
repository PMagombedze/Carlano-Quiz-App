"""
Authentication
"""

# primary key use uuid.uuid4()
from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route('auth/Login.action', strict_slashes=False)
def login():
    """home template"""
    return render_template('auth/login.html', strict_slashes=False)

@auth.route('auth/Registration.action')
def signup():
    """home template"""
    return render_template('auth/signup.html')
