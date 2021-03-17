import tkinter
from tkinter import *

top = Tk()

mb=  Menubutton (top, text="ABOUT US", relief=RAISED)
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label="Mikke",
                       variable=mayoVar )
mb.menu.add_checkbutton ( label="Pikke",
                          variable=ketchVar )

mb.pack()
top.mainloop()
