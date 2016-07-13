import numpy as np

def getCentroid(dataSTFT):
    a = 0.
    b = 0.
    for i in range(1, dataSTFT.size + 1):
        a = a + dataSTFT[i - 1] * i
        b = b + dataSTFT[i - 1]
    return a/b

def getRollOff(dataSTFT):
    data = np.sort(dataSTFT)
