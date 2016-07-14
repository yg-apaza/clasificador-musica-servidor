from audio import Audio
from feature import getFeatureVector
import pprint
import time

a = Audio(archivo='/home/yuli/pop.wav')
pp = pprint.PrettyPrinter(indent=4)

start = time.time()
print "> Cronometro iniciado"
test = getFeatureVector(a)
end = time.time()
print "> Fin de la ejecucion"
print "Tiempo: " + str(end - start) + " segundos"
print "----------------------------RESULTADOS---------------------------"
pp.pprint(test)
print "-----------------------------------------------------------------"
