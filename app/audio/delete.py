# import scipy.io.wavfile as wav
# import scipy.signal as signal
# import numpy as np
# from scipy.fftpack import fft
# import stft
from audio import Audio
from feature import getFeatureVector

a = Audio(archivo='/home/yuli/pop.wav')
getFeatureVector(a)
