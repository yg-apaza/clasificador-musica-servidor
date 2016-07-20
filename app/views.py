from app import app
from app import ALLOWED_EXTENSIONS
from app.dbconnect import conn
from app.audio.audioClass import Audio
from app.audio import feature
from app import common
from app.train import NEAT
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import pickle

cur = conn.cursor()
ANALYSIS_WINDOW = 512   # Ventana de analisis de 512 muestras
HOPSIZE = 256
TEXTURE_WINDOW = 86     # Nro de ventanas de analisis
NRO_TEXTURE_WINDOWS = 2584


@app.route('/entrenar', methods=['GET'])
def entrenar():
    NEAT.entrenar()
    winner = pickle.load(open(os.path.join(common.load('data_dir'),
                                           'redNeuronal.p'), 'r'))
    return str(winner)


@app.route('/', methods=['GET'])
def getLista():
    cur.execute("SELECT * FROM songs")
    rv = cur.fetchall()
    return render_template('lista.html', songs=rv)


@app.route('/agregar', methods=['POST'])
def agregarPost():
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
        audio = Audio(os.path.join(app.config['UPLOAD_FOLDER'], filename),
                      nro_texture_windows=NRO_TEXTURE_WINDOWS, hopsize=HOPSIZE)

        print '> Extrayendo caracteristicas:' + filename
        featureVector = feature.getFeatureVector(audio,
                                                 ANALYSIS_WINDOW,
                                                 HOPSIZE, TEXTURE_WINDOW)
        common.saveDict(featureVector,
                        os.path.join(app.config['UPLOAD_FOLDER'],
                                     filename + '.json'))
        print '> JSON generado: ' + filename + '.json'

        cur.execute(
            "INSERT INTO songs (filename, genre, data) VALUES (%s, %s, %s)",
            (filename, genero, filename + '.json'))
        conn.commit()

        return redirect(url_for('getLista'))


@app.route('/cancion/<id>')
def mostrarDatos(id):
    print id
    cur.execute("SELECT * FROM songs WHERE id=%s", (id,))
    rv = cur.fetchall()
    data = common.loadDict(os.path.join(app.config['UPLOAD_FOLDER'],
                           rv[0]['data']))
    return render_template('cancion.html', song=rv[0], data=data)

    # return str(common.loadDict(os.path.join(app.config['UPLOAD_FOLDER'],
    #                                        rv[0]['data'])))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
