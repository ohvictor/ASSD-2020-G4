from Python.Signals import Signal
from Python.Spectrum import Spectrum
from Python.Filters import Filters


class Component():
    def AA_filter(self, signal_in, filter):
        signal= Signal()
        signal = filter.Low_pass(signal_in)
        return signal


    def Sample_and_Hold(self, signal_in, clock):
        signal = Signal()
        spectrum = Spectrum()

        y = []
        x1, y1 = signal_in.get_time_data()
        x2, y2 = clock.get_time_data()

        y_hold = y1[0]

        for i in range(len(x1)):
            if y2[i] > 0:
                y.append(y_hold)
            else:
                y.append(y1[i])
                y_hold = y1[i]
        signal.set_time_data(x1, y)
        signal = spectrum.Fourier_transform(signal)
        return signal


    def Analog_switch(self, signal_in, clock):
        signal = Signal()
        spectrum = Spectrum()

        y = []
        x1, y1 = signal_in.get_time_data()
        x2, y2 = clock.get_time_data()

        for i in range(len(x1)):
            if y2[i] > 0:
                y.append(y1[i])
            else:
                y.append(0)

        signal.set_time_data(x1, y)
        signal = spectrum.Fourier_transform(signal)
        return signal


    def R_F(self, signal_in, filter):
        signal = Signal()
        signal = filter.Low_pass(signal_in)
        return signal


