from audio import Audio
import scipy.io.wavfile as wav
import scipy.signal as signal
import stft

a = Audio('/home/yuli/pop.wav')
# a.getSTFT()
fs, x = wav.read('/home/yuli/pop.wav')
stft.spectrogram(x,
                 framelength=512,
                 hopsize=256,
                 window=signal.hann,
                 centered=False,
                 halved=False)
