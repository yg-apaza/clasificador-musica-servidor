from flask import Flask
from app import common

ALLOWED_EXTENSIONS = set(['wav', 'mp3'])
MEDIA_ROOT = common.load('data_dir')
app = Flask(__name__)
app.secret_key = "mylittlepony"
app.config['UPLOAD_FOLDER'] = MEDIA_ROOT

from app import views
from app import dbconnect
