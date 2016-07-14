import numpy as np
from python_speech_features import mfcc


def getFeatureVector(audio, ANALYSIS_WINDOW, HOPSIZE, TEXTURE_WINDOW):
    data = audio.getSTFT(framesize=ANALYSIS_WINDOW, hopsize=HOPSIZE)
    features = np.empty([data.shape[0], 4])
    for i in range(0, data.shape[0]):
        # Centroide Espectral
        features[i, 0] = getCentroid(data[i])
        # RollOff
        features[i, 1] = getRollOff(data[i])
        # Flux
        features[i, 2] = getFlux(prev=data[i-1], current=data[i])
        # ZeroCrossings
        desde, hasta, add = audio.getFrame(frame=i, framesize=ANALYSIS_WINDOW,
                                           hopsize=HOPSIZE)
        amp = audio.data[desde:hasta]
        if add > 0:
            amp = np.append(amp, np.zeros(add))
        features[i, 3] = getZeroCrossings(amp)

    coef = getMFCC(audio.data, audio.fs, ANALYSIS_WINDOW, HOPSIZE)
    features = np.append(features, coef, axis=1)
    num_texture_windows = int(features.shape[0] / TEXTURE_WINDOW)
    features_mean_std = np.empty([num_texture_windows, 18])

    for i in range(0, num_texture_windows):
        mean = np.mean(features[i:i+TEXTURE_WINDOW, :],
                       axis=0, dtype=np.float64)
        std = np.std(features[i:i+TEXTURE_WINDOW, :], axis=0,
                     dtype=np.float64)
        features_mean_std[i, [0, 1, 2, 3, 4, 5, 6, 7, 8]] = mean
        features_mean_std[i, [9, 10, 11, 12, 13, 14, 15, 16, 17]] = std

    dict = {
        'mean-mean-Centroid':      np.mean(features_mean_std[:, 0],
                                           dtype=np.float64),
        'mean-std-Centroid':       np.mean(features_mean_std[:, 9],
                                           dtype=np.float64),
        'std-mean-Centroid':       np.std(features_mean_std[:, 0],
                                          dtype=np.float64),
        'std-std-Centroid':        np.std(features_mean_std[:, 9],
                                          dtype=np.float64),
        'mean-mean-RollOff':       np.mean(features_mean_std[:, 1],
                                           dtype=np.float64),
        'mean-std-RollOff':        np.mean(features_mean_std[:, 10],
                                           dtype=np.float64),
        'std-mean-RollOff':        np.std(features_mean_std[:, 1],
                                          dtype=np.float64),
        'std-std-RollOff':         np.std(features_mean_std[:, 10],
                                          dtype=np.float64),
        'mean-mean-Flux':          np.mean(features_mean_std[:, 2],
                                           dtype=np.float64),
        'mean-std-Flux':           np.mean(features_mean_std[:, 11],
                                           dtype=np.float64),
        'std-mean-Flux':           np.std(features_mean_std[:, 2],
                                          dtype=np.float64),
        'std-std-Flux':            np.std(features_mean_std[:, 11],
                                          dtype=np.float64),
        'mean-mean-ZeroCrossings': np.mean(features_mean_std[:, 3],
                                           dtype=np.float64),
        'mean-std-ZeroCrossings':  np.mean(features_mean_std[:, 12],
                                           dtype=np.float64),
        'std-mean-ZeroCrossings':  np.std(features_mean_std[:, 3],
                                          dtype=np.float64),
        'std-std-ZeroCrossings':   np.std(features_mean_std[:, 12],
                                          dtype=np.float64),
        'mean-mean-coeficiente1':  np.mean(features_mean_std[:, 4],
                                           dtype=np.float64),
        'mean-std-coeficiente1':   np.mean(features_mean_std[:, 13],
                                           dtype=np.float64),
        'std-mean-coeficiente1':   np.std(features_mean_std[:, 4],
                                          dtype=np.float64),
        'std-std-coeficiente1':    np.std(features_mean_std[:, 13],
                                          dtype=np.float64),
        'mean-mean-coeficiente2':  np.mean(features_mean_std[:, 5],
                                           dtype=np.float64),
        'mean-std-coeficiente2':   np.mean(features_mean_std[:, 14],
                                           dtype=np.float64),
        'std-mean-coeficiente2':   np.std(features_mean_std[:, 5],
                                          dtype=np.float64),
        'std-std-coeficiente2':    np.std(features_mean_std[:, 14],
                                          dtype=np.float64),
        'mean-mean-coeficiente3':  np.mean(features_mean_std[:, 6],
                                           dtype=np.float64),
        'mean-std-coeficiente3':   np.mean(features_mean_std[:, 15],
                                           dtype=np.float64),
        'std-mean-coeficiente3':   np.std(features_mean_std[:, 6],
                                          dtype=np.float64),
        'std-std-coeficiente3':    np.std(features_mean_std[:, 15],
                                          dtype=np.float64),
        'mean-mean-coeficiente4':  np.mean(features_mean_std[:, 7],
                                           dtype=np.float64),
        'mean-std-coeficiente4':   np.mean(features_mean_std[:, 16],
                                           dtype=np.float64),
        'std-mean-coeficiente4':   np.std(features_mean_std[:, 7],
                                          dtype=np.float64),
        'std-std-coeficiente4':    np.std(features_mean_std[:, 16],
                                          dtype=np.float64),
        'mean-mean-coeficiente5':  np.mean(features_mean_std[:, 8],
                                           dtype=np.float64),
        'mean-std-coeficiente5':   np.mean(features_mean_std[:, 17],
                                           dtype=np.float64),
        'std-mean-coeficiente5':   np.std(features_mean_std[:, 8],
                                          dtype=np.float64),
        'std-std-coeficiente5':    np.std(features_mean_std[:, 17],
                                          dtype=np.float64),
    }

    return dict


def getCentroid(data):
    a = 0.
    b = 0.
    dataMagnitude = np.abs(data)
    for i in range(1, dataMagnitude.size + 1):
        a = a + dataMagnitude[i - 1] * i
        b = b + dataMagnitude[i - 1]
    return a/b


def getRollOff(data):
    dataMagnitude = np.abs(data)
    sum = 0.85 * np.sum(dataMagnitude)
    count = 0
    for R in range(1, dataMagnitude.size + 1):
        if count > sum:
            break
        count += dataMagnitude[R - 1]
    return R


def getFlux(prev, current):
    if prev is None:
        prev = np.zeros(current.size)
    prevMagnitude = np.abs(prev)
    currentMagnitude = np.abs(current)
    sum = 0
    for i in range(0, currentMagnitude.size):
        sum += (currentMagnitude[i] - prevMagnitude[i]) ** 2
    return sum


def getZeroCrossings(data):
    sum = 0
    for i in range(0, data.size):
        sum += np.abs(np.sign(data[i]) - np.sign(data[i - 1]))
    return 0.5 * sum


def getMFCC(data, fs, ANALYSIS_WINDOW, HOPSIZE):
    coeficientes = mfcc(signal=data, samplerate=fs,
                        winlen=ANALYSIS_WINDOW*1./fs,
                        winstep=HOPSIZE*1./fs,
                        numcep=5)
    return coeficientes
