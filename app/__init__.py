from flask import Flask
from app import common

ALLOWED_EXTENSIONS = set(['wav', 'mp3'])
app = Flask(__name__, static_url_path='')
app.secret_key = "mylittlepony"
app.config['UPLOAD_FOLDER'] = common.load('data_dir')

from app import dbconnect
from app import views
