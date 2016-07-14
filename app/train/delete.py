from neat import nn
import pickle
from app.audio.audioClass import Audio
from app.audio import feature
from app import common


a = Audio('/home/yuli/generos/test/clasica/classical.00099.au.wav')
dict = feature.getFeatureVector(a, 512, 256, 86)

arr = common.featureDictToArray(dict)

winner = pickle.load(open('/home/yuli/IA2/clasificador/neuralNetwork.p', 'r'))
print(winner)
winner_net = nn.create_feed_forward_phenotype(winner)
output = winner_net.serial_activate(arr)

print output
