from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from flask_bcrypt import Bcrypt
from . import db, app
from flask_login import login_user, logout_user, login_required, current_user
import re
from EasyFlaskRecaptcha import ReCaptcha

recaptcha = ReCaptcha(app)
app.config.update(dict(
    GOOGLE_RECAPTCHA_ENABLED=True,
    GOOGLE_RECAPTCHA_SITE_KEY="6LdsZ5opAAAAAHQUPPtHtrjHl_TCe9acD5VLI6O6",
    GOOGLE_RECAPTCHA_SECRET_KEY="6LdsZ5opAAAAAOr4Rf2gI8yqtQE6TbPtu6ykwUDs",
    GOOGLE_RECAPTCHA_THEME = "light",
    GOOGLE_RECAPTCHA_TYPE = "image",
    GOOGLE_RECAPTCHA_SIZE = "normal",
    GOOGLE_RECAPTCHA_LANGUAGE = "en",
    GOOGLE_RECAPTCHA_RTABINDEX = 10,
))
recaptcha.init_app(app)

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
bcrypt = Bcrypt()

@auth.route('auth/Login.action', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.dashboard'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Email does not exist', category='error')

    referrer = request.referrer

    if referrer.endswith('/'):
        return render_template('auth/login.html', user=current_user)
    else:
        return render_template('auth/login_.html', user=current_user)

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
        if recaptcha.verify():
            if user:
                flash('Email already exists', category='error')
            elif is_secure_password(password) == False:
                flash('Password should contain at least a symbol and uppercase characters', category='warning')
            else:
                password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
                new_user = User(email=email, password=password_hash)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account created successfully', category='success')
                return redirect(url_for('views.dashboard'))
        else:
            flash('Recaptcha failed', category='error')


    return render_template('/auth/signup.html', user=current_user)