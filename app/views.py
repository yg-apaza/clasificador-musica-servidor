from flask import render_template, request, flash, redirect, url_for
from app import app
from app import ALLOWED_EXTENSIONS
from werkzeug.utils import secure_filename
import os


# Test line ;)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/song/add', methods=['POST'])
def addSong():
    url = request.form['url']
    genero = request.form['genero']
    print url
    print genero
    return render_template('lista.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/test', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'archivo' not in request.files:
            flash('No file part')
            print 'No file part'
            return redirect(request.url)
        file = request.files['archivo']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            print 'No selected file'
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print 'Uploaded file'
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=archivo>
         <input type=submit value=Upload>
    </form>
    '''
