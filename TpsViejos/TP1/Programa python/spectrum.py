import numpy as num
from signal import Signal
#Para obtener el espectro es fft y para obtener los puntos es el fftfreq
from numpy.fft import fft, fftfreq, ifft
#Para la prueba
import matplotlib.pylab as plt

class Spectrum:
    #devuelve el espectro de la funcion, pero es necesario que antes se haya realizado el espectro virgen
    def FT_1(self, S, pts):
        x_f, y_f = S.getFreqData_0()
        mask = x_f >= 0
        #Verdadero valores del espectro
        y_f = 2*num.abs(y_f/pts)
        #Se le agrega un 2 porque la mitad de las fuerza
        #original se encuentra distribuida entre la parte negativa y la parte positiva de las frecuencias
        S.setFreqData(x_f[mask], y_f[mask])
        return S

    #Devuelve el espectro de la funcion
    #En necesario darle tanto la señal original como la cantidad de tiempo (T) 
    #en el cual se lo va a mostrar junto con la cantidad total de puntos (pts)
    def FT(self, S, pts):
        x_t, y_t = S.getTimeData()
        x_f = fftfreq(pts, d = x_t[-1]/pts)
        y_f = fft(y_t) #Esta es la variable necesaria para una correcta antitranformada (aqui se obtiene el espectro virgen).}
        S.setFreqData_0(x_f, y_f)
        S = self.FT_1(S, pts)
        return S

    #Devuelva la funcion en el tiempo para esto suceda 
    def IFT(self, S, T, pts):
        x_t = num.linspace(0, T, pts)
        x_f, y_f = S.getFreqData_0()
        #Es necsario darle las cosas como salieron en principio de la 
        #tranformacion para la correcta antitransformada
        y_t = ifft(y_f)
        S.setTimeData(x_t, y_t)
        return S

# def main():
#     spec = Spectrum()
#     S = Signal()
#     n = 10000 #puntos totales en el tiempo
#     T=0.5 #tiempo que se va a mostrar la señal n seg
#     x = num.linspace(0,T,n)
#     y1 = 4.0*num.sin(4*2.0*num.pi*x)
#     y2 = 2.0*num.sin(8*2.0*num.pi*x)
#     y3 = 1.0*num.sin(20*2.0*num.pi*x)
#     y = y1 + y2 + y3
#     S.setTimeData(x, y)

#     plt.figure(1)
#     plt.title("Señal original")
#     plt.plot(S.getTimeData()[0], S.getTimeData()[1]) #plotea la señal original
#     plt.grid(True)

#     S = spec.FT(S,n)
#     plt.figure(2)
#     plt.title("Espectro")
#     plt.plot(S.getFreqData()[0], S.getFreqData()[1])
#     plt.grid(True)

#     S = spec.FT(S,n)
#     plt.figure(2)
#     plt.title("Espectro Virgen")
#     plt.plot(S.getFreqData_0()[0], S.getFreqData_0()[1])
#     plt.grid(True)
#     print(len(S.getFreqData_0()[0]))

#     S = spec.IFT(S, T, n)
#     plt.figure(4)
#     plt.title("Tiempo")
#     plt.plot(S.getTimeData()[0], S.getTimeData()[1])
#     plt.grid(True)
#     plt.show()

# #Para poder probar
# if __name__ == "__main__":
#     main()