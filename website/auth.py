"""
aunthentication (sign/signup/logout)
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, login_required, current_user


import re

commonPasswords = [
    123456,
    'password',
    123456789,
    12345678,
    12345,
    1234567,
    'admin',
    123123,
    'qwerty',
    'abc123',
    'letmein',
    'monkey',
    111111,
    'password1',
    'qwerty123',
    'dragon',
    1234,
    'baseball',
    'iloveyou',
    'trustno1',
    'sunshine',
    'princess',
    'football',
    'welcome',
    'shadow',
    'superman',
    'michael',
    'ninja',
    'mustang',
    'jessica',
    'charlie',
    'ashley',
    'bailey',
    'passw0rd',
    'master',
    'love',
    'hello',
    'freedom',
    'whatever',
    'nicole',
    'jordan',
    'cameron',
    'secret',
    'summer',
    '1q2w3e4r',
    'zxcvbnm',
    'starwars',
    'computer',
    'taylor',
    'startrek',
    123456,
    123456789,
    'qwerty',
    'password',
    12345,
    'qwerty123',
    '1q2w3e',
    12345678,
    111111,
    1234567890
]

def is_secure_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"\d",password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]",password):
        return False
    if password in commonPasswords:
        return False    
    return True

auth = Blueprint("auth", __name__)

@auth.route('auth/Login.action', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.dashboard'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template('/auth/login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('auth/Registration.action', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif is_secure_password(password) == False:
            flash('Password should contain at least a symbol and uppercase characters', category='warning')
        else:
            new_user = User(email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created successfully', category='success')
            return redirect(url_for('views.dashboard'))

    return render_template('/auth/signup.html', user=current_user)
