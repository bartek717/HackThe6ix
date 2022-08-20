from curses import flash
import curses
from unicodedata import category
from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    print()
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p> logout <p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        
        
    return render_template("sign_up.html")

