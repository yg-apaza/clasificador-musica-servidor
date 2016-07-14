from app import app
from app import ALLOWED_EXTENSIONS
from app.dbconnect import conn
from app.audio.audioClass import Audio
from app.audio import feature
from app import common
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

cur = conn.cursor()


@app.route('/song/add', methods=['GET'])
def addSongGet():
    return render_template('addSong.html')


@app.route('/', methods=['GET'])
def getLista():
    cur.execute("SELECT * FROM songs")
    rv = cur.fetchall()
    return render_template('lista.html', songs=rv)


@app.route('/song/add', methods=['POST'])
def addSongPost():
    genero = int(request.form['genero'])
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

        print '> Archivo subido: ' + filename
        audio = Audio(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        print '> Extrayendo caracteristicas:' + filename
        featureVector = feature.getFeatureVector(audio)
        common.saveDict(featureVector,
                        os.path.join(app.config['UPLOAD_FOLDER'],
                                     filename + '.json'))
        print '> JSON generado: ' + filename + '.json'

        cur.execute(
            "INSERT INTO songs (filename, genre, data) VALUES (%s, %s, %s)",
            (filename, genero, filename + '.json'))
        conn.commit()

        return redirect(url_for('getLista'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
