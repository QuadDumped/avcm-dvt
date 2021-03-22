from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
#from h5reader import groupItem, groupStructure

path = "log_210129_124838_1611920928.h5"

def selectedItem(item):
    print(item)

def plot(itemdata):

    fig = Figure(figsize=(4, 5), dpi=100)
    axes = fig.add_subplot(111)
    axes.plot([0,1,2,3,4], [10,1,20,3,40])
    canvas = FigureCanvasQTAgg(fig) 
    return canvas


