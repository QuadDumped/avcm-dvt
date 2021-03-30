from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
#from h5reader import groupItem, groupStructure

path = "log_210129_124838_1611920928.h5"

def selectedItem(item):
    print(item)

def createCanvas(fig):

    #axes.plot([1, 2000, 3000, 5000], [120000, 111000, 100000, 90000], "b")
    canvas = FigureCanvasQTAgg(fig) 
    return canvas


