import scipy.io.wavfile as wav
import scipy.signal as signal
import numpy as np
import stft


class Audio:
    def __init__(self, archivo=''):
        self.filename = archivo
        # convertir al formato estandar wav 22050Hz, 16 bits, 30 segs, mono
        # quitar ruido
        try:
            self.fs, self.data = wav.read(archivo)
            self.data = self.data/32767.
        except Exception:
            self.data = np.array([])

    def getSTFT(self, framesize=512, hopsize=256, window=signal.hann):
        espectograma = np.transpose(stft.spectrogram(self.data,
                                                     framelength=framesize,
                                                     hopsize=hopsize,
                                                     centered=False,
                                                     window=window,
                                                     halved=True))
        return espectograma

    def getFrame(self, frame=0, framesize=512, hopsize=256):
        desde = frame * hopsize
        hasta = desde + framesize
        add = 0
        if hasta > self.data.size:
            add = hasta - self.data.size
            hasta = self.data.size
        return (desde, hasta, add)
