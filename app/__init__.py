from flask import Flask
import os

ALLOWED_EXTENSIONS = set(['wav', 'mp3'])
MEDIA_ROOT = os.environ.get('OPENSHIFT_DATA_DIR', '')
app = Flask(__name__)
app.secret_key = "mylittlepony"
app.config['UPLOAD_FOLDER'] = MEDIA_ROOT

from app import views
from app import dbconnect
