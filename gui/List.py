import tkinter
from tkinter import *
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def embeddedPlot(X, Y):
    fig = Figure(figsize = (5, 5), dpi = 100) 
    plot1 = fig.add_subplot(111) 
    plot1.plot(X, Y)

    canvas = FigureCanvasTkAgg(fig, master = window)   
    canvas.draw() 
    canvas.get_tk_widget().pack()

x = [1, 2, 3, 4]
y = [1, 2, 3, 6]

window = Tk()
window.geometry("600x300")
window.title("A graph") 

mb = Menubutton (window, text="Signals", relief=RAISED)
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton ( label="Signal 1", variable=mayoVar)
mb.menu.add_checkbutton ( label="Signal 2", variable=ketchVar)
mb.pack(side = TOP, anchor=NW)

embeddedPlot(x, y)

window.mainloop()


