#para la gui
import tkinter as tk
#para el ploteo
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pylab as plt
#otros
from TP1.Python.signal  import Signal
from TP1.Python.generator import Generator
from TP1.Python.filter import Filter
from TP1.Python.block import Block

class Gui:
    def __init__(self): #constructor.
        #defino la ventana.
        self.__window = tk.Tk()
        self.__window.title("ASSD - TP1")
        self.__window.geometry("1250x665+50+25")
        self.__window.configure(bg="gray80")

        #defino el plano para plotear en el tiempo,
        self.__fig_t = Figure(figsize = (6, 4))
        self.__plt_t = self.__fig_t.add_subplot(1,1,1) #los dos primeros parámetros le da una escala a la figura (mientras más grandes son los parámetros, mas chico será la figura). El tercero le da la posición en el self.window.
        self.__plt_t.set_title("SIGNAL IN TIME")
        self.__plt_t.set_xlabel("Time(mSec)")
        self.__plt_t.set_ylabel("Amp(V)")
        #self.axes_t = self.__fig.gca()
        self.__graph_t = FigureCanvasTkAgg(self.__fig_t, master = self.__window)
        self.__graph_t._tkcanvas.place(x = 10, y = 10)
        __frame_t = tk.Frame()
        __frame_t.place(x = 10, y = 0)
        __nav_t = NavigationToolbar2Tk(self.__graph_t, __frame_t)
        __nav_t.update()

        #defino el plano para plotear en la frecuencia.
        self.__fig_f = Figure(figsize = (6, 4))
        self.__plt_f = self.__fig_f.add_subplot(1, 1, 1) #los dos primeros parámetros le da una escala a la figura (mientras más grandes son los parámetros, mas chico será la figura). El tercero le da la posición en el self.window.
        self.__plt_f.set_title("SIGNAL IN FREQUENCY")
        self.__plt_f.set_xlabel("Freq(KHz)")
        self.__plt_f.set_ylabel("Amp(V)")
        #self.axes_f = fig.gca()
        self.__graph_f = FigureCanvasTkAgg(self.__fig_f, master = self.__window)
        self.__graph_f._tkcanvas.place(x = 640, y = 10) #plotea el plot.
        __frame_f = tk.Frame()
        __frame_f.place(x = 640, y = 0)
        __nav_f = NavigationToolbar2Tk(self.__graph_f, __frame_f)
        __nav_f.update()

        #cargo la imagen del circuito.
        self.__circuit = tk.Canvas(self.__window, width = 800, height = 125, bg = "gray80", highlightthickness = 0) #highlightthickness = 0 -> removes de default outline of the canvas.
        self.__circuit.place(x = 375, y = 470)
        self.__circ_img = tk.PhotoImage(file = "circuit.png")
        self.__circuit.create_image(5, 5, anchor = tk.NW, image = self.__circ_img)

        #defino los botonos de switch.
        self.__b_switch = [] #arreglo de botones de los switches.
        self.__arr_img = [] #arreglo de las imagenes de las flechas (iran dentro de los botones).
        self.__switch_st = [] #arreglo de los etados de cada switch (0 -> bypass, 1-> no bypass).
        for i in range(4):
            self.__b_switch.append(tk.Button(self.__window))
            self.__b_switch[i].place(x = 520 + i*188, y = 519)
            self.__arr_img.append(tk.PhotoImage(file = "arrowup.png"))
            self.__b_switch[i].config(anchor = tk.N, image = self.__arr_img[i], bg = "gray70")
            self.__switch_st.append(0)
        self.__b_switch[0].config(height = 40, command = self.switch0_move)
        self.__b_switch[1].config(height = 40, command = self.switch1_move)
        self.__b_switch[2].config(height = 40, command = self.switch2_move)
        self.__b_switch[3].config(height = 40, command = self.switch3_move)

        #defino los botones para ver las señales en los nodos.
        self.__b_signal = [] #arreglo de botones de los nodos.
        self.__signal_st = [] #arreglo de los estados de cada nodo (0 -> no plot, 1 -> plot).
        self.__s_color = ["red", "green", "blue", "yellow", "magenta", "cyan"]
        for i in range(6):
            self.__b_signal.append(tk.Button(self.__window))
            self.__b_signal[i].config(bg = "gray70")
            self.__signal_st.append(0)
            if i > 0 and i < 4:
                self.__b_signal[i].place(x = 389 + i*188, y = 460)
        self.__b_signal[0].place(x = 360, y = 536)
        self.__b_signal[0].config(text = "S0", command = self.plot_signal0)
        self.__b_signal[1].config(text = "S1", command = self.plot_signal1)
        self.__b_signal[2].config(text = "S2", command = self.plot_signal2)
        self.__b_signal[3].config(text = "S3", command = self.plot_signal3)
        self.__b_signal[4].place(x = 1155, y = 536)
        self.__b_signal[4].config(text = "S4", command = self.plot_signal4)
        self.__b_signal[5].place(x = 360, y = 580)
        self.__b_signal[5].config(text = "S5", command = self.plot_signal5)

        #organizo los seteos para la señal analogica y digital.
        __label1 = tk.Label(self.__window, font = ("arial",10,"bold"), text = "ANALOG SIGNAL(S0):", bg = "gray80")
        __label1.place(x = 70, y = 420)
        __label11 = tk.Label(self.__window, font = ("arial", 10), text = "type = ", bg = "gray80")
        __label11.place(x = 80, y = 445)
        __label12 = tk.Label(self.__window, font = ("arial", 10), text = "Freq(KHz) = ", bg = "gray80")
        __label12.place(x = 80, y = 470)
        __label13 = tk.Label(self.__window, font = ("arial", 10), text = "Amp(V) = ", bg = "gray80")
        __label13.place(x = 80, y = 495)
        self.__s_type = tk.Spinbox(self.__window, width = 10, state = "readonly", values = ("sin()", "cos()", "3/2sin()", "sinc()", "AM()"))
        self.__s_type.place(x = 160, y = 445)
        self.__entry12 = tk.Entry(self.__window, width = 10)
        self.__entry12.place(x = 160, y = 470)
        self.__entry13 = tk.Entry(self.__window, width = 10)
        self.__entry13.place(x = 160, y = 495)
        __label2 = tk.Label(self.__window, font = ("arial",10,"bold"), text = "DIGITAL SIGNAL(S5):", bg = "gray80")
        __label2.place(x = 70, y = 525)
        __label21 = tk.Label(self.__window, font = ("arial", 10), text = "Freq(KHz) = ", bg = "gray80")
        __label21.place(x = 80, y = 550)
        __label22 = tk.Label(self.__window, font = ("arial", 10), text = "DC(%) = ", bg = "gray80")
        __label22.place(x = 80, y = 575)
        self.__entry21 = tk.Entry(self.__window, width = 10)
        self.__entry21.place(x = 160, y = 550)
        self.__entry22 = tk.Entry(self.__window, width = 10)
        self.__entry22.place(x = 160, y = 575)
        __label3 = tk.Label(self.__window, font = ("arial",10,"bold"), text = "LOW PASS FILTER(AAF,RF):", bg = "gray80")
        __label3.place(x = 70, y = 605)
        __label31 = tk.Label(self.__window, font = ("arial", 10), text = "Freq(KHz) = ", bg = "gray80")
        __label31.place(x = 80, y = 630)
        self.__entry31 = tk.Entry(self.__window, width = 10)
        self.__entry31.place(x = 160, y = 630)
        self.__ready = 0 #si ready = 0 -> no podemos plotear, si ready = 1 -> podemos plotear.
        __b_ready = tk.Button(self.__window) #boton para plotear
        __b_ready.config(text = "READY", width = 10, height = 11, bg = "gray70", command = self.ready_to_plot)
        __b_ready.place(x = 265, y = 445)
        self.__warning = tk.Label(self.__window, font = ("arial",10,"bold"), text = "ERROR: Make sure you have set the values correctly.", bg = "gray80", fg="red3")

        #defino el generador de funciones y las señales que estaran en cada nodo.
        self.__gen = Generator()
        self.__fil = Filter()
        self.__block = Block()
        self.__signal = [] #arreglo de los botones de cada nodo.
        for i in range(6):
            self.__signal.append(Signal())
        

    def loop (self):
        self.__window.mainloop()
    
    def switch0_move (self):
        if self.__ready == 1:
            if self.__switch_st[0] == 0:
                self.__arr_img[0] = tk.PhotoImage(file = "arrowdown.png")
                self.__b_switch[0].config(anchor = tk.S, image = self.__arr_img[0])
                self.__switch_st[0] = 1
            elif self.__switch_st[0] == 1:
                self.__arr_img[0] = tk.PhotoImage(file = "arrowup.png")
                self.__b_switch[0].config(anchor = tk.N, image = self.__arr_img[0])
                self.__switch_st[0] = 0
            self.__update_calc()
            self.__update_plot()

    def switch1_move (self):
        if self.__ready == 1:
            if self.__switch_st[1] == 0:
                self.__arr_img[1] = tk.PhotoImage(file = "arrowdown.png")
                self.__b_switch[1].config(anchor = tk.S, image = self.__arr_img[1])
                self.__switch_st[1] = 1
            elif self.__switch_st[1] == 1:
                self.__arr_img[1] = tk.PhotoImage(file = "arrowup.png")
                self.__b_switch[1].config(anchor = tk.N, image = self.__arr_img[1])
                self.__switch_st[1] = 0
            self.__update_calc()
            self.__update_plot()
    
    def switch2_move (self):
        if self.__ready == 1:
            if self.__switch_st[2] == 0:
                self.__arr_img[2] = tk.PhotoImage(file = "arrowdown.png")
                self.__b_switch[2].config(anchor = tk.S, image = self.__arr_img[2])
                self.__switch_st[2] = 1
            elif self.__switch_st[2] == 1:
                self.__arr_img[2] = tk.PhotoImage(file = "arrowup.png")
                self.__b_switch[2].config(anchor = tk.N, image = self.__arr_img[2])
                self.__switch_st[2] = 0
            self.__update_calc()
            self.__update_plot()

    def switch3_move (self):
        if self.__ready == 1:
            if self.__switch_st[3] == 0:
                self.__arr_img[3] = tk.PhotoImage(file = "arrowdown.png")
                self.__b_switch[3].config(anchor = tk.S, image = self.__arr_img[3])
                self.__switch_st[3] = 1
            elif self.__switch_st[3] == 1:
                self.__arr_img[3] = tk.PhotoImage(file = "arrowup.png")
                self.__b_switch[3].config(anchor = tk.N, image = self.__arr_img[3])
                self.__switch_st[3] = 0
            self.__update_calc()
            self.__update_plot()

    def plot_signal0 (self):
        if self.__ready == 1:
            if self.__signal_st[0] == 0:
                self.__b_signal[0].config(bg = self.__s_color[0])
                self.__signal_st[0] = 1
            elif self.__signal_st[0] == 1:
                self.__b_signal[0].config(bg = "gray70")
                self.__signal_st[0] = 0
            self.__update_plot()

    def plot_signal1 (self):
        if self.__ready == 1:
            if self.__signal_st[1] == 0:
                self.__b_signal[1].config(bg = self.__s_color[1])
                self.__signal_st[1] = 1
            elif self.__signal_st[1] == 1:
                self.__b_signal[1].config(bg = "gray70")
                self.__signal_st[1] = 0
            self.__update_plot()

    def plot_signal2 (self):
        if self.__ready == 1:
            if self.__signal_st[2] == 0:
                self.__b_signal[2].config(bg = self.__s_color[2])
                self.__signal_st[2] = 1
            elif self.__signal_st[2] == 1:
                self.__b_signal[2].config(bg = "gray70")
                self.__signal_st[2] = 0
            self.__update_plot()

    def plot_signal3 (self):
        if self.__ready == 1:
            if self.__signal_st[3] == 0:
                self.__b_signal[3].config(bg = self.__s_color[3])
                self.__signal_st[3] = 1
            elif self.__signal_st[3] == 1:
                self.__b_signal[3].config(bg = "gray70")
                self.__signal_st[3] = 0
            self.__update_plot()

    def plot_signal4 (self):
        if self.__ready == 1:
            if self.__signal_st[4] == 0:
                self.__b_signal[4].config(bg = self.__s_color[4])
                self.__signal_st[4] = 1
            elif self.__signal_st[4] == 1:
                self.__b_signal[4].config(bg = "gray70")
                self.__signal_st[4] = 0
            self.__update_plot()

    def plot_signal5 (self):
        if self.__ready == 1:
            if self.__signal_st[5] == 0:
                self.__b_signal[5].config(bg = self.__s_color[5])
                self.__signal_st[5] = 1
            elif self.__signal_st[5] == 1:
                self.__b_signal[5].config(bg = "gray70")
                self.__signal_st[5] = 0
            self.__update_plot()

    def ready_to_plot (self):
        try: #se fija si alguna de las especificaciones está vacio o no es un número.
            float(self.__entry12.get())
            float(self.__entry13.get())
            float(self.__entry21.get())
            float(self.__entry22.get())
            float(self.__entry31.get())
        except ValueError:
            self.__warning.place(x = 300, y = 630)
            return
        if float(self.__entry22.get()) < 1 or float(self.__entry22.get()) > 99:
            self.__warning.place(x = 300, y = 630)
            return
        if float(self.__entry12.get()) <= 0 or float(self.__entry13.get()) <= 0:
            self.__warning.place(x = 300, y = 630)
            return
        if float(self.__entry21.get()) <= 0 or float(self.__entry22.get()) <= 0:
            self.__warning.place(x = 300, y = 630)
            return
        if float(self.__entry31.get()) <= 0:
            self.__warning.place(x = 300, y = 630)
            return

        self.__warning.place_forget()
        self.__ready = 1
        if self.__s_type.get() == "sin()":
            self.__signal[0] = self.__gen.gen_sin(float(self.__entry13.get()), float(self.__entry12.get()), 4/(float(self.__entry12.get())), 100000)
            self.__signal[5] = self.__gen.gen_square(5, float(self.__entry21.get()), float(self.__entry22.get()), 4/(float(self.__entry12.get())), 100000)
        elif self.__s_type.get() == "cos()":
            self.__signal[0] = self.__gen.gen_cos(float(self.__entry13.get()), float(self.__entry12.get()), 4/(float(self.__entry12.get())), 100000)
            self.__signal[5] = self.__gen.gen_square(5, float(self.__entry21.get()), float(self.__entry22.get()), 4/(float(self.__entry12.get())), 100000)
        elif self.__s_type.get() == "3/2sin()":
            self.__signal[0] = self.__gen.gen_3_2sin(float(self.__entry13.get()), float(self.__entry12.get()), 4/(float(self.__entry12.get())), 100000)
            self.__signal[5] = self.__gen.gen_square(5, float(self.__entry21.get()), float(self.__entry22.get()), 4/(float(self.__entry12.get())), 100000)
        elif self.__s_type.get() == "sinc()":
            self.__signal[0] = self.__gen.gen_sinc(float(self.__entry13.get()), float(self.__entry12.get()), 4/(float(self.__entry12.get())), 100000)
            self.__signal[5] = self.__gen.gen_square(5, float(self.__entry21.get()), float(self.__entry22.get()), 4/(float(self.__entry12.get())), 100000)
        elif self.__s_type.get() == "AM()":
            self.__signal[0] = self.__gen.gen_AM(float(self.__entry13.get()), float(self.__entry12.get()), 5*4/(float(self.__entry12.get())), 100000)
            self.__signal[5] = self.__gen.gen_square(5, float(self.__entry21.get()), float(self.__entry22.get()), 5*4/(float(self.__entry12.get())), 100000)
        self.__fil.set_LPfreq(float(self.__entry31.get()))
        self.__b_signal[4].config(bg = self.__s_color[4])
        self.__signal_st[4] = 1
        self.__update_calc()
        self.__update_plot()
        

    def __update_plot(self):
        self.__plt_t.clear()
        self.__plt_t.set_title("SIGNAL IN TIME")
        self.__plt_t.set_xlabel("Time(mSec)")
        self.__plt_t.set_ylabel("Amp(V)")
        self.__plt_f.clear()
        self.__plt_f.set_title("SIGNAL IN FREQUENCY")
        self.__plt_f.set_xlabel("Freq(KHz)")
        self.__plt_f.set_ylabel("Amp(V)")
        self.__plt_f.set_xlim(0, 50*self.__signal[0].freq)
        for i in range(6):
            if self.__signal_st[i] == 1:
                self.__plt_t.plot(self.__signal[i].getTimeData()[0], self.__signal[i].getTimeData()[1], color = self.__s_color[i])
                self.__plt_f.plot(self.__signal[i].getFreqData()[0], self.__signal[i].getFreqData()[1], color = self.__s_color[i])
        self.__graph_t.draw()
        self.__graph_f.draw()
    
    def __update_calc(self):
        if self.__switch_st[0] == 1:
            self.__signal[1] = self.__block.AAF(self.__signal[0], self.__fil)
        else:
            self.__signal[1] = self.__signal[0]
        if self.__switch_st[1] == 1:
            self.__signal[2] = self.__block.SH(self.__signal[1], self.__signal[5])
        else:
            self.__signal[2] = self.__signal[1]
        if self.__switch_st[2] == 1:
            self.__signal[3] = self.__block.SWI(self.__signal[2], self.__signal[5])
        else:
            self.__signal[3] = self.__signal[2]
        if self.__switch_st[3] == 1:
            self.__signal[4] = self.__block.RF(self.__signal[3], self.__fil)
        else:
            self.__signal[4] = self.__signal[3]

def main ():
    gui = Gui()
    gui.loop()

if __name__ == "__main__":
    main()