import numpy as num
from scipy import signal as sign
from TP1.Python.signal import Signal
from TP1.Python.spectrum import Spectrum
#for test
import matplotlib.pyplot as plt

class Filter:
    def __init__(self):
        self.__LPfreq = 0
    
    def set_LPfreq(self, LPfreq):
        self.__LPfreq = LPfreq
    
    def LP(self, S1):
        S = Signal()
        spect = Spectrum()
        x1, y1 = S1.getFreqData_0()
        y = y1
        for i in range(len(x1)):
            if x1[i] <= -self.__LPfreq or x1[i] >= self.__LPfreq:
                y[i] = 0
        S.setFreqData_0(x1, y)
        S = spect.FT_1(S, len(S1.getTimeData()[0]))
        S = spect.IFT(S, S1.getTimeData()[0][-1], len(S1.getTimeData()[0])) #[-1] -> hace referencia al ultimo elemento.
        return S

def main():
    pts = 100000
    T = 5

    S1= Signal()
    freq1 = 1
    Vmax1 = 5
    x1_t = num.linspace(0, T, pts) #genera puntos equiespaciados linealmente.
    y1_t = num.multiply(Vmax1, num.sin(num.multiply(2*num.pi*freq1, x1_t)))
    S1.setTimeData(x1_t, y1_t)

    spect = Spectrum()
    S1 = spect.FT(S1, pts)

    x_f = S1.getFreqData_0()[0]
    s = num.multiply(2j*num.pi, x_f)
    H = s
    for i in range(len(x_f)):
        H[i] = (1)/(s[i]/(2*num.pi*10) + 1)

    # print(len(S1.getFreqData_0()[0]))
    # print(len(H))
    S2 = Signal()
    y_f = s
    for i in range(pts):
        if i < int(pts/2):
            y_f[i] = H[i]*S1.getFreqData_0()[1][int(pts/2) + i]
        else:
            y_f[i] = H[i]*S1.getFreqData_0()[1][i - int(pts/2)]
    #y_f = num.multiply(S1.getFreqData_0()[1], H)
    print(S1.getFreqData_0()[0][int(0)])
    print(x_f[int(0)])
    print(S1.getFreqData_0()[0][int(pts/2)])
    print(x_f[int(pts/2)])
    print(S1.getFreqData_0()[0][int(pts)-1])
    print(x_f[int(pts)-1])
    print(S2.getTimeData())
    S2.setFreqData_0(x_f, y_f)
    S2 = spect.FT_1(S2, pts)
    S2 = spect.IFT(S2, T, pts)

    plt.figure(1)
    plt.title("Tiempo1")
    plt.plot(S1.getTimeData()[0], S1.getTimeData()[1])
    plt.grid(True)

    plt.figure(2)
    plt.title("Tiempo2")
    plt.plot(S2.getTimeData()[0], S2.getTimeData()[1])
    plt.grid(True)

    plt.figure(3)
    plt.title("frecuencia1")
    plt.plot(S2.getFreqData()[0], S2.getFreqData()[1])
    plt.grid(True)

    plt.show()



# #Para poder probar
if __name__ == "__main__":
    main()