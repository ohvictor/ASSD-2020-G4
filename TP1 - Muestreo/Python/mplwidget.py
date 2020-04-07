from PyQt5.QtWidgets import *

from PyQt5 import QtGui

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

import numpy as np

from webcolors import *
from scipy import signal

class MplWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # Esto detecta color background y se lo pone a la figura del grafico (asi es generico)
        color = self.palette().color(QtGui.QPalette.Background)
        color.red(), color.green(), color.blue()
        hex = rgb_to_hex((color.red(), color.green(), color.blue()))

        self.fig = Figure(facecolor=hex)
        self.fig.savefig("image_filename.png", edgecolor=self.fig.get_edgecolor())

        self.canvas = FigureCanvas(self.fig)

        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.set_facecolor("#e1ddbf")
        self.setLayout(layout)

    def plot(self, signal, key):
        self.canvas.axes.clear()
        if key == 'time':
            self.canvas.axes.plot(signal.get_time_data()[0], signal.get_time_data()[1])
            self.canvas.axes.legend()
            self.canvas.draw()
        else:
            self.canvas.axes.plot(signal.get_frequency_data()[0], signal.get_frequency_data()[1])
            self.canvas.axes.legend()
            self.canvas.draw()



    def clear_axes(self):
        self.canvas.axes.clear()
        self.canvas.draw()