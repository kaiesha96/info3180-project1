import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import os
DB_URL = 'postgres://lzlorkmcthykcd:3db001dd773617858680304cc6235e3558e22b61ca2c2e7808870a21258d40c0@ec2-54-235-146-51.compute-1.amazonaws.com:5432/d6lciq3mhj2b2m'
DEBUG = True
SQL_TRACK = True
SECRET = os.urandom(24)
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