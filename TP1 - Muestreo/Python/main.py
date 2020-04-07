from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import sys


##This code makes exceptions appear when sometimes pyqt wraps them in some rnadom error number
sys._excepthook = sys.excepthook

def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

sys.excepthook = my_exception_hook

#########


from Python.Signals import Signal
from Python.Generator import Generator
from Python.Filters import Filters
from Python.Components import Component

from Python.Mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        ##Aca van los callbacks

        self.ui.pushButton_configure.clicked.connect(self.update_signals)
       # self.ui.pushButton_1.clicked.connect(lambda: self.update_grafico('prueba'))
        #self.ui.pushButton_2.clicked.connect()
        #self.ui.pushButton_3.clicked.connect()
        #self.ui.pushButton_4.clicked.connect()
        #self.ui.pushButton_5.clicked.connect()
        #self.ui.pushButton_6.clicked.connect()

        #########################

        self.generator = Generator()
        self.components = Component()
        self.filter = Filters()
        self.signals = []
        for i in range(6):
            self.signals.append(Signal())


    def update_signals(self):
        self.error_checking()
        self.asign_signals()
        self.checkboxes()

    def checkboxes(self):
        if self.ui.checkBox_1.isChecked():
            self.signals[1] = self.components.AA_filter(self.signals[0], self.filter)

            self.ui.line_2.setStyleSheet('background-color: rgb(255, 255, 255)')
            self.ui.line_3.setStyleSheet('background-color: rgb(255, 255, 255)')
            self.ui.line_b1.move(300, 150)
            self.ui.line_b1.resize(43, self.ui.line_b1.height())
        else:
            self.signals[1] = self.signals[0]

            self.ui.line_2.setStyleSheet('background-color: rgb(0, 0, 0)')
            self.ui.line_3.setStyleSheet('background-color: rgb(0, 0, 0)')
            self.ui.line_b1.move(320, 150)
            self.ui.line_b1.resize(65, self.ui.line_b1.height())

        if self.ui.checkBox_2.isChecked():
            self.signals[2] = self.components.Sample_and_Hold(self.signals[1], self.signals[5])

            self.ui.line_4.setStyleSheet('background-color: rgb(255, 255, 255)')
            self.ui.line_8.setStyleSheet('background-color: rgb(255, 255, 255)')
            self.ui.line_b2.move(520, 150)
            self.ui.line_b2.resize(43, self.ui.line_b2.height())
        else:
            self.signals[2] = self.signals[1]

            self.ui.line_4.setStyleSheet('background-color: rgb(0, 0, 0)')
            self.ui.line_8.setStyleSheet('background-color: rgb(0, 0, 0)')
            self.ui.line_b2.move(540, 150)
            self.ui.line_b2.resize(65, self.ui.line_b2.height())

        if self.ui.checkBox_3.isChecked():
            self.signals[3] = self.components.Analog_switch(self.signals[2], self.signals[5])

            self.ui.line_10.setStyleSheet('background-color: rgb(255, 255, 255)')
            self.ui.line_11.setStyleSheet('background-color: rgb(255, 255, 255)')
            self.ui.line_b3.move(740, 150)
            self.ui.line_b3.resize(43, self.ui.line_b3.height())
        else:
            self.signals[3] = self.signals[2]

            self.ui.line_10.setStyleSheet('background-color: rgb(0, 0, 0)')
            self.ui.line_11.setStyleSheet('background-color: rgb(0, 0, 0)')
            self.ui.line_b3.move(760, 150)
            self.ui.line_b3.resize(65, self.ui.line_b3.height())

        if self.ui.checkBox_4.isChecked():
            self.signals[4] = self.components.R_F(self.signals[3], self.filter)

            self.ui.line_14.setStyleSheet('background-color: rgb(255, 255, 255)')
            self.ui.line_15.setStyleSheet('background-color: rgb(255, 255, 255)')
            self.ui.line_16.setStyleSheet('background-color: rgb(255, 255, 255)')
            self.ui.line_b4_2.move(960, 150)
            self.ui.line_b4_2.resize(85, self.ui.line_b4_2.height())
        else:
            self.signals[4] = self.signals[3]

            self.ui.line_14.setStyleSheet('background-color: rgb(0, 0, 0)')
            self.ui.line_15.setStyleSheet('background-color: rgb(0, 0, 0)')
            self.ui.line_16.setStyleSheet('background-color: rgb(0, 0, 0)')
            self.ui.line_b4_2.move(980, 150)
            self.ui.line_b4_2.resize(65, self.ui.line_b4_2.height())


    def asign_signals(self):
        sinput = str(self.ui.comboBox.currentText())

        sin_amp = float(self.ui.lineEdit_amplitude_sin.text())
        sin_freq = float(self.ui.lineEdit_frequency_sin.text())
        clock_freq = float(self.ui.lineEdit_frequency_control.text())
        clock_dc = float(self.ui.lineEdit_dc_control.text())



        if sinput == 'Sin()':
            self.signals[0] = self.generator.generate_sin(sin_amp, sin_freq, 4/sin_freq, 100000)
            self.signals[5] = self.generator.generate_square(5, clock_freq, clock_dc, 4/sin_freq, 100000)
        elif sinput == 'Cos()':
            self.signals[0] = self.generator.generate_cos(sin_amp,sin_freq, 4/sin_freq, 100000)
            self.signals[5] = self.generator.generate_square(5, clock_freq, clock_dc, 4/sin_freq, 100000)
        elif sinput == '3/2Sin()':
            self.signals[0] = self.generator.generate_32_sin(sin_amp, sin_freq, 4/sin_freq, 100000)
            self.signals[5] = self.generator.generate_square(5, clock_freq, clock_dc, 4/sin_freq, 100000)
        elif sinput == 'Sinc()':
            self.signals[0] = self.generator.generate_sinc(sin_amp, sin_freq, 4/sin_freq, 100000)
            self.signals[5] = self.generator.generate_square(5, clock_freq, clock_dc, 4/sin_freq, 100000)
        elif sinput == 'AM()':
            self.signals[0] = self.generator.generate_AM(sin_amp, sin_freq, 5 * 4/sin_freq, 100000)
            self.signals[5] = self.generator.generate_square(5, clock_freq, clock_dc, 5 * 4/sin_freq, 100000)

        self.filter.set_frequency(float(self.ui.lineEdit_frequency_filter.text()))

    def error_checking(self):
        try:
            float(self.ui.lineEdit_frequency_sin.text())
            float(self.ui.lineEdit_amplitude_sin.text())
            float(self.ui.lineEdit_frequency_control.text())
            float(self.ui.lineEdit_dc_control.text())
            float(self.ui.lineEdit_frequency_filter.text())
        except ValueError:
            self.show_pop_up('Be sure to be entering the data correctly')

        dc = float(self.ui.lineEdit_dc_control.text())
        if dc < 1 or dc > 99:
            self.show_pop_up('Duty Cicle must be a number between 1 and 99')

        freq_signal = float(self.ui.lineEdit_frequency_sin.text())
        if freq_signal <= 0:
            self.show_pop_up('Frequencies must be positive! Or should they?')

        amp_signal = float(self.ui.lineEdit_amplitude_sin.text())
        if amp_signal <= 0:
            self.show_pop_up('Amplitudes must be positive!')

        freq_clock = float(self.ui.lineEdit_frequency_control.text())
        if freq_clock <= 0:
            self.show_pop_up('Negative Frequencies dont exist... in the real world')

        freq_filter = float(self.ui.lineEdit_frequency_filter.text())
        if freq_filter <= 0:
            self.show_pop_up('The filter frequency you entered is non-positive!')

    def update_grafico(self, signal):

        self.ui.time_domain.plot(signal, 'time')
        self.ui.frequency_domain(signal, 'frequency')

    def show_pop_up(self, error):
        msg = QMessageBox()
        msg.setWindowTitle('Mistakes were made')
        msg.setText(error)
        msg.setIcon(QMessageBox.Warning)

        x = msg.exec_()

# Controlador de ventanas, conecta señales que le dicen a las distintas ventanas cuando abrirse y cerrarse
class Controller:

    def __init__(self):
        pass

    def show_main(self):
        self.window = MainWindow()
        self.window.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()