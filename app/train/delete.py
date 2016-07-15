from neat import nn
import pickle
from app.audio.audioClass import Audio
from app.audio import feature
from app import common


a = Audio('/home/yuli/TM.wav',
          nro_texture_windows=2584, hopsize=256)
dict = feature.getFeatureVector(a, 512, 256, 86)

arr = common.featureDictToArray(dict)

winner = pickle.load(open('/home/yuli/IA2/clasificador/app/data/redNeuronal.p',
                          'r'))
winner_net = nn.create_feed_forward_phenotype(winner)
output = winner_net.serial_activate(arr)

print output
