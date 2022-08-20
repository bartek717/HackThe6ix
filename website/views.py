from flask import Blueprint, render_template
from flask_login import  login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/upload')
@login_required
def upload():
    return render_template("upload.html", user=current_user)

@views.route('/overview')
@login_required
def overview():
    return render_template("overview.html", user=current_user)

@views.route('/view')
@login_required
def view():
    return render_template("view.html", user=current_user)
    

