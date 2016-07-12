from flask import render_template, request, redirect, url_for
from app import app
from app import ALLOWED_EXTENSIONS
from werkzeug.utils import secure_filename
from app.dbconnect import conn
import os

cur = conn.cursor()


@app.route('/add')
def index():
    # cur.execute("SELECT * FROM songs")
    # rv = cur.fetchall()
    # print str(rv)
    return render_template('index.html')


@app.route('/', methods=['GET'])
def getLista():
    cur.execute("SELECT * FROM songs")
    rv = cur.fetchall()
    return render_template('lista.html', songs=rv)


@app.route('/song/add', methods=['POST'])
def addSong():
    # genero = request.form['genero']
    if 'archivo' not in request.files:
        print 'No se ha enviado ningun archivo'
        return redirect(url_for('index'))
    file = request.files['archivo']
    if file.filename == '':
        print 'No se ha seleccionado ningun archivo'
        return redirect(url_for('index'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print 'Archivo subido !'

        # cur.execute("INSERT INTO songs (filename, genre) VALUES (%s, %s)",
        #           (file.filename, genero))
        # conn.commit()

        return redirect(url_for('getLista'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
