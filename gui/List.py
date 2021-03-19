import tkinter
from tkinter import *
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def embeddedPlot(X = [1, 2, 3, 4], Y = [1, 2, 3, 6]):

    fig = Figure(figsize = (5, 5), dpi = 100) 
    plot1 = fig.add_subplot(111) 
    plot1.plot(X, Y)

    canvas = FigureCanvasTkAgg(fig, master = window)   
    canvas.draw() 
    canvas.get_tk_widget().pack()


window = Tk()
window.geometry("600x300")
window.title("A graph") 

mb = Menubutton (window, text="Signals", relief=RAISED)
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mayoVar = IntVar()
ketchVar = IntVar()
button1 = mb.menu.add_checkbutton ( label="Signal 1", variable=mayoVar, command= lambda: embeddedPlot([1, 2, 3, 4], [1, 3, 5, 1]))
button2 = mb.menu.add_checkbutton ( label="Signal 2", variable=ketchVar, command= lambda: embeddedPlot())

mb.pack(side = TOP, anchor=NW)
 

window.mainloop()


