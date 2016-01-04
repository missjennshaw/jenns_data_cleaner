from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import pickle
import os


UPLOAD_FOLDER = os.getcwd()+"/uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
from app import views
