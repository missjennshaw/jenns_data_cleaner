from flask import render_template, redirect,request,url_for,g,send_from_directory
from app import app
from datetime import datetime
import json
import math
import os
from werkzeug import secure_filename
from tools import split_csv, name_spliter

ALLOWED_EXTENSIONS = ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/",methods=["GET","POST"])
def ingestion_engine():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            local_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(local_file)
            split_csv(local_file)
    return render_template("ingestion_engine.html")





