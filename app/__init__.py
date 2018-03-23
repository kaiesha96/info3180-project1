import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from config import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.debug = DEBUG
app.secret_key = SECRET
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQL_TRACK

db = SQLAlchemy(app)
CSRF_ENABLED = DEBUG
UPLOAD_FOLDER="./app/static/uploads"
ALLOWED_EXTENSIONS = {"png", 'jpg', 'jpeg', 'gif'}

app.config.from_object(__name__)

from app import views