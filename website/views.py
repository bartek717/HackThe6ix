import json
from flask import Blueprint, render_template,request
from flask_login import  login_required, current_user
from  website.read_receipts import read_receipt
import datetime
import io

from .models import Receipt
from . import db

from PIL import Image

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/upload',methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        img = request.files['file']
        in_memory_file = io.BytesIO()
        img.save(in_memory_file)
        img = Image.open(in_memory_file)
        total, subtotal, taxes, items = read_receipt(img)
        data = {
            'total':total,
            'subtotal':subtotal,
            'subtotal':subtotal,
            'taxes':taxes,
            'items':items
        }
        user_id = current_user.id
        data = json.dumps(data)
        new_receipt =Receipt(data=data,date=datetime.datetime.now(),user_id=user_id)
        db.session.add(new_receipt)
        db.session.commit()

    return render_template("upload.html", user=current_user)

@views.route('/overview')
@login_required
def overview():
    return render_template("overview.html", user=current_user)

def get_all_receipt_from(user_id):
    receipts = Receipt.query.filter_by(user_id=user_id).all()
    return receipts

@views.route("/get")
@login_required
def json_api():
    receipts = get_all_receipt_from(current_user.id)
    return [json.loads(receipt.data) for receipt in receipts]

@views.route('/view')
@login_required
def view():
    return render_template("view.html", user=current_user)
    