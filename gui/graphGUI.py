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


app = QApplication([])
app.setStyle("Fusion")

window = QWidget()
layout = QVBoxLayout()

combo = QComboBox()
groupItems = groupStructure('0 VCM1')
for item in groupItems:
    combo.addItem(item)

#hämta data från valt item och skicka in det i plot
currentItem = combo.currentText
itemData = "null" #groupItem(currentItem)
canvas = plot(itemData)

#kopplar selectedItem till knapparna och skriver ut item i terminalen
combo.activated[str].connect(selectedItem) 

layout.addWidget(combo)
layout.addWidget(canvas)
window.setLayout(layout)
window.show()
app.exec()

