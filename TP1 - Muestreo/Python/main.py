from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import sys

from Python.Mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        ##Aca van los callbacks

        self.ui.pushButton_configure.clicked.connect()
        self.ui.pushButton_1.clicked.connect(lambda: self.update_grafico('prueba'))
        self.ui.pushButton_2.clicked.connect()
        self.ui.pushButton_3.clicked.connect()
        self.ui.pushButton_4.clicked.connect()
        self.ui.pushButton_5.clicked.connect()
        self.ui.pushButton_6.clicked.connect()

        #########################

        self.checkboxes_state = [0, 0, 0, 0]


    def update_grafico(self, signal):

        self.ui.time_domain.plot(signal, 'time')
        self.ui.frequency_domain(signal, 'frequency')

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