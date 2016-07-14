import json
import os
import numpy as np


def load(var):
    # with open('settingsOpenshift.json') as data_file:
    with open(os.path.join(os.path.dirname(__file__),
                           'settings.json')) as data_file:
        data = json.load(data_file)
    if data[var]['type'] == 'env':
        return os.environ.get(data[var]['value'], '')
    elif data[var]['type'] == 'var':
        return data[var]['value']
    else:
        return ""


def saveDict(dict, filename):
    with open(filename, 'w') as fp:
        json.dump(dict, fp)


def loadDict(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data


def featureDictToArray(dict):
    arr = np.empty(len(dict))
    arr[0] = dict['mean-mean-Centroid']
    arr[1] = dict['mean-std-Centroid']
    arr[2] = dict['std-mean-Centroid']
    arr[3] = dict['std-std-Centroid']
    arr[4] = dict['mean-mean-RollOff']
    arr[5] = dict['mean-std-RollOff']
    arr[6] = dict['std-mean-RollOff']
    arr[7] = dict['std-std-RollOff']
    arr[8] = dict['mean-mean-Flux']
    arr[9] = dict['mean-std-Flux']
    arr[10] = dict['std-mean-Flux']
    arr[11] = dict['std-std-Flux']
    arr[12] = dict['mean-mean-ZeroCrossings']
    arr[13] = dict['mean-std-ZeroCrossings']
    arr[14] = dict['std-mean-ZeroCrossings']
    arr[15] = dict['std-std-ZeroCrossings']
    arr[16] = dict['mean-mean-coeficiente1']
    arr[17] = dict['mean-std-coeficiente1']
    arr[18] = dict['std-mean-coeficiente1']
    arr[19] = dict['std-std-coeficiente1']
    arr[20] = dict['mean-mean-coeficiente2']
    arr[21] = dict['mean-std-coeficiente2']
    arr[22] = dict['std-mean-coeficiente2']
    arr[23] = dict['std-std-coeficiente2']
    arr[24] = dict['mean-mean-coeficiente3']
    arr[25] = dict['mean-std-coeficiente3']
    arr[26] = dict['std-mean-coeficiente3']
    arr[27] = dict['std-std-coeficiente3']
    arr[28] = dict['mean-mean-coeficiente4']
    arr[29] = dict['mean-std-coeficiente4']
    arr[30] = dict['std-mean-coeficiente4']
    arr[31] = dict['std-std-coeficiente4']
    arr[32] = dict['mean-mean-coeficiente5']
    arr[33] = dict['mean-std-coeficiente5']
    arr[34] = dict['std-mean-coeficiente5']
    arr[35] = dict['std-std-coeficiente5']
    return arr
