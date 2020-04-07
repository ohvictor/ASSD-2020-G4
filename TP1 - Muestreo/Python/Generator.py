import numpy as np
from Python.Signals import Signal
from Python.Spectrum import Spectrum

import matplotlib.pylab as plt

class Generator():

    def generate_cos(self, Vmax, frequency, T, length):
        signal = Signal()
        spectrum = Spectrum()

        signal.set_frequency(frequency)

        x_t = np.linspace(0, T, length)
        y_t = np.multiply(Vmax,np.cos(np.multiply(2 * np.pi * frequency, x_t)))

        signal.set_time_data(x_t, y_t)
        S = spectrum.Fourier_transform(signal)
        return signal

    def generate_sin(self, Vmax, frequency, T, length):
        signal = Signal()
        spectrum = Spectrum()

        signal.set_frequency(frequency)

        x_t = np.linspace(0, T, length)
        y_t = np.multiply(Vmax, np.sin(np.multiply(2 * np.pi * frequency, x_t)))

        signal.set_time_data(x_t, y_t)

        signal = spectrum.Fourier_transform(signal)

        return signal

    def generate_32_sin(self, Vmax, frequency, T, length):
        signal = Signal()
        spectrum = Spectrum()

        signal.set_frequency(frequency)

        x_t = np.linspace(0, T, length)
        y_t = []

        var = 0
        for i in range(len(x_t)):
            if x_t[i] >= (var + 1) / frequency:
                var += 1
            y_t.append(Vmax * np.sin(1.5 * 2 * np.pi * frequency * (x_t[i] - var / frequency)))

        signal.set_time_data(x_t, y_t)
        signal = spectrum.Fourier_transform(signal)

        return signal

    def generate_square(self, Vmax, frequency, DC, T, length):
        signal = Signal()
        spectrum = Spectrum()

        signal.set_frequency(frequency)

        x_t = np.linspace(0, T, length)
        y_t = []

        var = 0
        for i in range(len(x_t)):
            if x_t[i] >= (var + 1) / frequency:
                var += 1
            if (x_t[i] - var / frequency) >= DC / (100 * frequency):
                y_t.append(0)
            else:
                y_t.append(Vmax)

        signal.set_time_data(x_t, y_t)
        signal = spectrum.Fourier_transform(signal)

        return signal

    def generate_sinc(self, Vmax, frequency, T, length):
        signal = Signal()
        spectrum = Spectrum()

        signal.set_frequency(frequency)

        x_t = np.linspace(0, T, length)
        y_t = []

        var = 0
        for i in range(len(x_t)):
            if x_t[i] >= (var + 1) / frequency:
                var = var + 1
            y_t.append(Vmax * np.sinc(8 * frequency * (x_t[i] - var / frequency) - 4))

        signal.set_time_data(x_t, y_t)
        signal = spectrum.Fourier_transform(signal)
        return signal

    def generate_AM(self, Vmax, frequency, T, length):
        signal = Signal()
        spectrum = Spectrum()

        signal.set_frequency(frequency)

        x_t = np.linspace(0, T, length)
        y_t = []

        y_t = np.multiply(Vmax, np.multiply(1/2, np.cos(np.multiply(2 * np.pi* 1.8 * frequency, x_t))) + np.cos(np.multiply(2 * np.pi * 2 *frequency, x_t)) + np.multiply(1/2, np.cos(np.multiply(2 * np.pi * 2.2 *frequency, x_t))))

        signal.set_time_data(x_t, y_t)
        signal = spectrum.Fourier_transform(signal)
        return signal