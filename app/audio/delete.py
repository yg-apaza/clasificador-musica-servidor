from app.audio.audioClass import Audio
from app.audio.feature import getFeatureVector
from app import common
import pprint
import time


a = Audio(archivo='/home/yuli/metal.wav')
pp = pprint.PrettyPrinter(indent=4)

print "> Cronometro iniciado"
start = time.time()
test = getFeatureVector(a)
common.saveDict(test, 'test.json')
end = time.time()
print "> Fin de la ejecucion"
print "Tiempo: " + str(end - start) + " segundos"
print "----------------------------RESULTADOS---------------------------"
pp.pprint(test)
print "-----------------------------------------------------------------"
