import scipy.io.wavfile as wav
import scipy.signal as signal
import numpy as np
from scipy.fftpack import fft
import stft
from audio import Audio


def getData(filename):
    '''
    audio = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    espectograma = np.transpose(stft.spectrogram(audio,
                                                 framelength=4,
                                                 hopsize=2,
                                                 window=signal.hann,
                                                 centered=False,
                                                 halved=False))
    print espectograma
    '''
    a = Audio('/home/yuli/pop.wav')
    print a.getSTFT().shape
    print a.data.shape
    print a.getFrame(frame=2584)
getData('/home/yuli/pop.wav')
