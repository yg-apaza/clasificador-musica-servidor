import scipy.io.wavfile as wav
import scipy.signal as signal
import numpy as np
import stft
import matplotlib.pyplot as plt


class Audio:
    def __init__(self, archivo=''):
        self.filename = archivo
        # convertir al formato estandar wav 22050Hz, 16 bits, 30 segs, mono
        # quitar ruido
        try:
            self.fs, self.data = wav.read(archivo)
            self.data = self.data/32767.
            # plt.plot(self.data)
            # plt.show()
        except Exception:
            self.data = np.array([])

    def getSTFT(self, framesize=512, hopsize=256, window=signal.hann):
        '''
        i = 0
        espectograma = np.array([np.zeros(framesize)])
        while i < self.data.size:
            residuo = (i + framesize) - self.data.size
            if residuo > 0:
                frame = np.append(self.data[i:self.data.size],
                                  np.zeros(residuo))
            else:
                frame = self.data[i:i+framesize]

            if i == 0:
                espectograma = np.array([fft(frame * window(framesize))])
            else:
                espectograma = np.append(espectograma,
                                         np.array([fft(frame *
                                                   window(framesize))]),
                                         axis=0)
            i += hopsize
        return espectograma
        '''
        espectograma = np.transpose(stft.spectrogram(self.data,
                                                     framelength=framesize,
                                                     hopsize=hopsize,
                                                     centered=False,
                                                     window=window,
                                                     halved=False))
        return espectograma

    def getFrame(self, frame=0, framesize=512, hopsize=256):
        desde = frame * hopsize
        hasta = desde + framesize
        add = 0
        if hasta > self.data.size:
            add = hasta - self.data.size
            hasta = self.data.size
        return (desde, hasta, add)
