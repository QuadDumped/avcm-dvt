import h5py
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from gui.graphGUI import plot, selectedItem
from h5reader import groupStructure, retrieveGroups


#selectedgroup = h5reader.retrieveGroups()[0]
#print(h5reader.groupStructure(selectedgroup))

app = QApplication([])
app.setStyle("Fusion")

window = QWidget()
layout = QVBoxLayout()

combo = QComboBox()

firstGroup = retrieveGroups()[0]
groupItems = groupStructure(firstGroup)
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