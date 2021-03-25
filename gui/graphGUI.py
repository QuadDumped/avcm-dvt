from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
#from h5reader import groupItem, groupStructure

path = "log_210129_124838_1611920928.h5"

def selectedItem(item):
    print(item)

def plot(itemdata):

    x = []
    y = []
    i = 0

    for row in itemdata:
        i+=1
        x.append(i)
        y.append(row[1])

    fig = Figure(figsize=(5, 5), dpi=100)
    axes = fig.add_subplot(111)
    axes.plot(x, y)
    canvas = FigureCanvasQTAgg(fig) 
    return canvas


