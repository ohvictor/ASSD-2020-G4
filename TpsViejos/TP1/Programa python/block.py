import math
from signal import Signal
from spectrum import Spectrum
from filter import Filter
import matplotlib.pylab as plt

class Block:
    #simula la tarea del AAF.
    def AAF(self, S1, fil): #S1 -> señal de entrada, fil -> filtro.
        S = Signal()
        S = fil.LP(S1)
        return S

    #simula la tarea del S&H.
    def SH(self, S1, S2): #S1 -> señal de entrada, S2 -> CLK.
        S = Signal()
        spect = Spectrum()
        y = []
        x1, y1 = S1.getTimeData()
        x2, y2 = S2.getTimeData()
        yh = y1[0]
        for i in range(len(x1)):
            if y2[i] > 0:
                y.append(yh)
            else:
                y.append(y1[i])
                yh = y1[i]
        S.setTimeData(x1, y)
        S = spect.FT(S, len(x1))
        return S
        

    #simula la tarea de la llave analogica.
    def SWI(self, S1, S2): #S1 -> señal de entrada, S2 -> CLK.
        S = Signal()
        spect = Spectrum()
        y = []
        x1, y1 = S1.getTimeData()
        x2, y2 = S2.getTimeData()
        for i in range(len(x1)):
            if y2[i] > 0:
                y.append(y1[i])
            else:
                y.append(0)
        S.setTimeData(x1, y)
        S = spect.FT(S, len(x1)) 
        return S

    #simula la tarea del RF.
    def RF(self, S1, fil): #S1 -> señal de entrada, fil -> filtro.
        S = Signal()
        S = fil.LP(S1)
        return S