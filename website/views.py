from flask import Blueprint, render_template,request
from flask_login import  login_required, current_user
from  website.read_recipts import read_receipt
import io
from PIL import Image


views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/upload',methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        photo = request.files['file']
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        img = Image.open(in_memory_file)
        read_receipt(img)

    return render_template("upload.html", user=current_user)

@views.route('/overview')
@login_required
def overview():
    return render_template("overview.html", user=current_user)

@views.route('/view')
@login_required
def view():
    return render_template("view.html", user=current_user)
    