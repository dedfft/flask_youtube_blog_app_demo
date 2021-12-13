from flask import Blueprint,render_template, redirect, url_for, request, flash
from models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    email = request.form.get('email')
    password1 = request.form.get('password')
    return render_template('login.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()
        if email_exists:
            flash('Email Exists')
        elif username_exists:
            flash('Username already in user')
        elif password1 != password2:
            flash('Passwords do not match')
        else:
            new_user = User(email=email, username=username, password=password1)
            db.session.add(new_user)
            db.session.commit()
            flash('user created')
            return redirect(url_for('views.home'))


    return render_template('sign_up.html')


@auth.route('/logout')
def logout():
    return redirect(url_for("views.home"))