class Signal:
    def __init__(self):
        self.x_t= 0
        self.y_t = 0
        self.x_f = 0
        self.y_f = 0
        self.original_x_f = 0
        self.original_y_f = 0
        self.freq = 0

    def set_frequency(self, frequency):
        self.freq = frequency

    def set_time_data(self, x_t, y_t):
        self.x_t = x_t
        self.y_t = y_t

    def set_frequency_data(self, x_f, y_f):
        self.x_f = x_f
        self.y_f = y_f

    def set_originial_frequency_data(self, x_f, y_f):
        self.original_x_f = x_f
        self.original_y_f = y_f

    def get_time_data(self):
        return self.x_t, self.y_t

    def get_frequency_data(self):
        return self.x_f, self.y_f

    def get_original_frequency_data(self):
        return self.original_x_f, self.original_y_f