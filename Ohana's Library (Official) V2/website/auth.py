from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Note, Theme
from . import db 
from werkzeug.security import generate_password_hash, check_password_hash
import requests

auth = Blueprint('auth', __name__)

@auth.route('/welcome')
def welcome():
    theme = Theme.query.filter_by(id=0).first()
    return render_template("welcome.html", user=current_user, theme = theme)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    theme = Theme.query.filter_by(id=0).first()
    if request.method == 'POST':
        username  = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Loged In successfully!', category='success')
                login_user(user, remember=True)

                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user, theme=theme)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.test'))

@auth.route('/logout_login')
def test():
    theme = Theme.query.filter_by(id=0).first()
    return render_template("logout.html", user=current_user, theme = theme)

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    theme = Theme.query.filter_by(id=0).first()
    if request.method == 'POST':
        username = request.form.get('username')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exist.', category='error')
        elif len(username) < 1:
            flash('Username must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 1 characters', category='error')
        elif password1 != password2:
            flash('Password don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 characters', category='error')
        else:
            new_user = User(username=username, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user, theme=theme)