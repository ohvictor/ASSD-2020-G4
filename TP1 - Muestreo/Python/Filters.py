from Python.Signals import Signal
from Python.Spectrum import Spectrum
import matplotlib.pyplot as plt
import numpy as np

class Filters():
    def __init__(self):
        self.fa = 0

    def set_frequency(self, fa):
        self.fa = fa

    def Low_pass(self, original_signal):
        signal = Signal()
        spectrum = Spectrum()

        length = len(original_signal.get_time_data()[0])

        x_1, y_1 = original_signal.get_original_frequency_data()
        y = y_1

        for i in range(len(x_1)):
            if x_1[i] <= -self.fa or x_1[i] >= self.fa:
                y[i] = 0

        signal.set_originial_frequency_data(x_1, y)

        signal = spectrum.Original_Fourier_transform(signal, length)
        signal = spectrum.Inverse_Fourier_transform(signal, original_signal.get_time_data()[0][-1], len(original_signal.get_time_data()[0]))
        return signal
