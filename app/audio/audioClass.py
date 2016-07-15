import scipy.io.wavfile as wav
import scipy.signal as signal
import numpy as np
import stft
from pydub import AudioSegment


class Audio:
    def __init__(self, archivo='', nro_texture_windows=1, hopsize=256):
        self.filename = archivo
        # convertir al formato estandar wav 22050Hz, 16 bits, 30 segs, mono
        # quitar ruido
        song = AudioSegment.from_wav(archivo)
        newb = song.high_pass_filter(500)
        newa = newb.low_pass_filter(500)
        newa.export(archivo, format="wav")

        try:
            self.fs, self.data = wav.read(archivo)
            self.data = self.data/32767.

            if(self.data.size > nro_texture_windows * hopsize):
                self.data = self.data[0:nro_texture_windows * hopsize]
            elif (self.data.size < nro_texture_windows * hopsize):
                add = nro_texture_windows * hopsize - self.data.size
                self.data = np.append(self.data, np.zeros(add))
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
