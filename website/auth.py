"""
aunthentication (sign/signup/logout)
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, login_required, current_user
from security.securePasswordChecker import is_secure_password

auth = Blueprint("auth", __name__)

@auth.route('/signin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email1')
        password = request.form.get('password1')

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

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        passwordCfrm = request.form.get('passwordCfrm')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif is_secure_password(password) == False:
            flash('Password should contain at least a symbol and uppercase characters', category='warning')
        elif password != passwordCfrm:
            flash('Passwords did not match', category='error')
        else:
            new_user = User(email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created successfully', category='success')
            return redirect(url_for('views.dashboard'))

    return render_template('/auth/signup.html', user=current_user)
