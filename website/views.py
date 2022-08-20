from flask import Blueprint, render_template, request, Response
from werkzeug.utils import secure_filename
from flask_login import  login_required, current_user
from db import db_init, db
from models import Img

views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
@login_required
def home():
    
    return render_template("home.html", user=current_user)

