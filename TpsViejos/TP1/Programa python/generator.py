import numpy as num
import math
from signal import Signal
from spectrum import Spectrum
import matplotlib.pylab as plt

class Generator:
    #realiza la multiplicacion de 2 señales en el tiempo y a la vez las convoluciona en frecuencia.
    def multiply_signals(self, S1, S2):
        S = Signal()
        x1_t, y1_t = S1.getTimeData()
        x2_t, y2_t = S2.getTimeData()
        y3_t = num.multiply(y1_t, y2_t)
        S.setTimeData(x1_t, y3_t)

        x1_f, y1_f = S1.getFreqData()
        x2_f, y2_f = S2.getFreqData()
        y3_f = num.convolve(y1_f,y2_f)
        S.setFreqData(x1_f, y3_f)
        return S
    
    #realiza la convolucion de 2 señales en el tiempo y a la vez las multiplica en frecuencia.
    def convol_signals(self, S1, S2):
        S = Signal()
        x1_t, y1_t = S1.getTimeData()
        x2_t, y2_t = S2.getTimeData()
        y3_t = num.convolve(y1_t, y2_t)
        S.setTimeData(x1_t, y3_t)

        x1_f, y1_f = S1.getFreqData()
        x2_f, y2_f = S2.getFreqData()
        y3_f = num.multiply(y1_f,y2_f)
        S.setFreqData(x1_f, y3_f)
        return S

    #freq -> frecuencia, T -> intervalo a plotear, pts -> los puntos en el intervalo.
    def gen_sin(self, Vmax, freq, T, pts):
        S = Signal()
        spect = Spectrum()
        S.freq = freq
        x_t = num.linspace(0, T, pts) #genera puntos equiespaciados linealmente.
        y_t = num.multiply(Vmax, num.sin(num.multiply(2*num.pi*freq, x_t)))
        S.setTimeData(x_t, y_t)
        S = spect.FT(S, pts)
        return S
    
    #freq -> frecuencia, T -> intervalo a plotear, pts -> los puntos en el intervalo.
    def gen_cos(self, Vmax, freq, T, pts):
        S = Signal()
        spect = Spectrum()
        S.freq = freq
        x_t = num.linspace(0, T, pts) #genera puntos equiespaciados linealmente.
        y_t = num.multiply(Vmax,num.cos(num.multiply(2*num.pi*freq, x_t)))
        S.setTimeData(x_t, y_t)
        S = spect.FT(S, pts)
        return S

    #freq -> frecuencia, T -> intervalo a plotear, pts -> los puntos en el intervalo.
    def gen_3_2sin(self, Vmax, freq, T, pts):
        S = Signal()
        spect = Spectrum()
        temp = 0 #me ayudara generar el 3/2sen.
        S.freq = freq
        y_t = []
        x_t = num.linspace(0, T, pts)
        for i in range(len(x_t)):
            if x_t[i] >= (temp + 1)/freq:
                temp = temp + 1
            y_t.append(Vmax*num.sin(1.5*2*num.pi*freq*(x_t[i] - temp/freq)))
        S.setTimeData(x_t, y_t)
        S = spect.FT(S, pts)
        return S

    #freq -> frecuencia, DC -> duty cycle de la señal en %, T -> intervalo a plotear, pts -> los puntos en el intervalo.
    def gen_square(self, Vmax, freq, DC, T, pts):
        S = Signal()
        spect = Spectrum()
        temp = 0 #me ayudara generar la cuadrada.
        y_t = []
        S.freq = freq
        x_t = num.linspace(0, T, pts) #genera puntos equiespaciados linealmente.
        for i in range(len(x_t)):
            if x_t[i] >= (temp + 1)/freq:
                temp = temp + 1
            if (x_t[i] - temp/freq) >= DC/(100*freq):
                y_t.append(0)
            else:    
                y_t.append(Vmax)
        S.setTimeData(x_t, y_t)
        S = spect.FT(S, pts)
        return S

    #f -> frecuencia, N_T -> numero de peridos que se quiere plotear, n -> puntos por periodo (para plotear).
    def gen_sinc(self, Vmax, freq, T, pts):
        S = Signal()
        spect = Spectrum()
        temp = 0 #me ayudara generar la sinc.
        y_t = []
        S.freq = freq
        x_t = num.linspace(0, T, pts)
        for i in range(len(x_t)):
            if x_t[i] >= (temp + 1)/freq:
                temp = temp + 1
            y_t.append(Vmax*num.sinc(8*freq*(x_t[i] - temp/freq) - 4))
        S.setTimeData(x_t, y_t)
        S = spect.FT(S, pts)
        return S
    
    #f -> frecuencia, N_T -> numero de peridos que se quiere plotear, n -> puntos por periodo (para plotear).
    def gen_AM(self, Vmax, freq, T, pts):
        S = Signal()
        spect = Spectrum()
        temp = 0 #me ayudara generar la sinc.
        y_t = []
        S.freq = freq
        x_t = num.linspace(0, T, pts)
        y_t = num.multiply(Vmax, num.multiply(1/2, num.cos(num.multiply(2*num.pi*1.8*freq, x_t))) + num.cos(num.multiply(2*num.pi*2*freq, x_t)) + num.multiply(1/2, num.cos(num.multiply(2*num.pi*2.2*freq, x_t))))
        S.setTimeData(x_t, y_t)
        S = spect.FT(S, pts)
        return S

#Para realizar la prueba
def main():
    gen = Generator()
    S0 = Signal()
    S1 = Signal()
    S2 = Signal()
    S3 = Signal()
    S4 = Signal()

    #S0 = gen.gen_sin(1, 2, 4/2, 10000)
    #S1 = gen.gen_3_2sin(1, 4, 4/4, 10000)
    #S2 = gen.gen_square(5, 3.25, 50, 4/2, 10000)
    S3 = gen.gen_sinc(2, 1, 1/1, 10000)
    #S4 = gen.gen_AM(2, 1, 5*1/1, 10000)
    #plt.plot(S0.getTimeData()[0], S0.getTimeData()[1])
    #plt.plot(S1.getTimeData()[0], S1.getTimeData()[1])
    #plt.plot(S2.getTimeData()[0], S2.getTimeData()[1])
    plt.plot(S3.getTimeData()[0], S3.getTimeData()[1])
    #plt.plot(S4.getTimeData()[0], S4.getTimeData()[1])
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()