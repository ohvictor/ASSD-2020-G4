import numpy as num

class Signal:
    def __init__(self):
        self.__x_f_0 = 0
        self.__x_f = 0
        self.__x_t = 0
        self.__y_f_0 = 0
        self.__y_f = 0
        self.__y_t = 0
        self.freq = 0

    def setTimeData(self, x_t, y_t):
        self.__x_t = x_t
        self.__y_t = y_t

    def setFreqData(self, x_f, y_f):
        self.__x_f = x_f
        self.__y_f = y_f
    
    def setFreqData_0(self, x_f_0, y_f_0): #mantiene el espectro virgen.
        self.__x_f_0 = x_f_0
        self.__y_f_0 = y_f_0

    def getFreqData_0(self): #devuelve el espectro virgen.
        return self.__x_f_0, self.__y_f_0

    def getTimeData(self):
        return self.__x_t, self.__y_t

    def getFreqData(self):
        return self.__x_f, self.__y_f 