from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from app.dbconnect import conn
from app import common
from app.audio.audioClass import Audio
from app.audio import feature
import numpy as np
import os
from pybrain.supervised.trainers import BackpropTrainer

net = buildNetwork(36, 20, 4, bias=True)
ds = SupervisedDataSet(36, 4)
print "FIRST  ----------------------------------------"
print net
cur = conn.cursor()
cur.execute("SELECT * FROM songs")
rv = cur.fetchall()

for i in range(0, len(rv)):
    dict = common.loadDict(os.path.join(common.load('data_dir'),
                           rv[i]['data']))
    arr = common.featureDictToArray(dict)
    # inputsTrain[i, :] = arr
    temp = np.zeros(4)
    temp[int(rv[i]['genre']) - 1] = 1
    ds.addSample(tuple(arr), tuple(temp))
    # outputsTrain[i, :] = temp

trainer = BackpropTrainer(net, ds)
trainer.train()
print "SECOND  ----------------------------------------"
print net
ab = Audio('/home/yuli/generos/metal/metal.00015.au.wav',
           nro_texture_windows=2584, hopsize=256)
d = feature.getFeatureVector(ab, 512, 256, 86)

arr = common.featureDictToArray(dict)

out = net.activate(arr)
print out
