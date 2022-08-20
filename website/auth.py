from curses import flash
import curses
from unicodedata import category
from flask import Blueprint, render_template, request, redirect, url_for,flash
from website import views
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                print("Logged in successfully")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                error = "Unable to authenticate"
                flash(error)
        else:
            error = "User does not exist"
            flash(error)
    return render_template("auth/login.html")


@auth.route('/logout')
@login_required
def logout():
    """
    If the user is logged in, log them out and redirect them to the home page
    :return: a redirect to the home page.
    """
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('views.home'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if password1!=password2:
            error = "Please confirm your password."
            flash(error)
            return render_template("sign_up.html")

        user = User.query.filter_by(email=email).first()
        if user:
            error = "Email already registered."
            flash(error)
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('views.home'))
        
    return render_template("auth/sign_up.html", user=current_user)