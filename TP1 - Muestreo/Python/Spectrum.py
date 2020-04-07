import numpy as np
from numpy.fft import fft, fftfreq, ifft
from Python.Signals import Signal

class Spectrum():

    #With this function que truncate the spectrum tothe nn negative part.
    def Original_Fourier_transform(self, signal, length):
        x_f, y_f = signal.get_original_frequency_data()

        mask = x_f >= 0

        y_f = 2 * np.abs(y_f / length)

        signal.set_frequency_data(x_f[mask], y_f[mask])
        return signal


    #Resturns original signal with its full spectrum
    def Fourier_transform(self, signal):
        x_t, y_t = signal.get_time_data()

        length = len(signal.get_time_data()[0])
        x_f = fftfreq(length, d=x_t[-1] / length)
        y_f = fft(y_t)

        signal.set_originial_frequency_data(x_f, y_f)
        #Until here we have the full spectrum, but we need only the positive part

        signal = self.Original_Fourier_transform(signal, length)
        return signal

    #Returns time signal
    def Inverse_Fourier_transform(self, signal, T, length):
        x_t = np.linspace(0, T, length)
        x_f, y_f = signal.get_original_frequency_data()

        y_t = ifft(y_f)

        signal.set_time_data(x_t, y_t)
        return signal
