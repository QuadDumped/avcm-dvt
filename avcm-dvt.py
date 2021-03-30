import h5py
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox, QFileDialog, QLayout, QHBoxLayout, QMessageBox, QButtonGroup
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from tkinter import filedialog
from gui.graphGUI import plot, selectedItem
from h5reader import groupStructure, retrieveGroups, groupItem, readData

#selectedGroup = h5reader.retrieveGroups()[0]
#selectedItem = h5reader.groupStructure(selectedGroup)[0]
#datasetValues = h5reader.readData(selectedGroup, selectedItem)
#print(datasetValues)

#selectedgroup = h5reader.retrieveGroups()[0]
#print(h5reader.groupStructure(selectedgroup))

app = QApplication([])
app.setStyle("Fusion")

window = QWidget()
window.setWindowTitle("Autonomous Vehicle Controle Module Data Visualization Tool")
window.setFixedWidth(1280)
window.setFixedHeight(800)

#window är strukturerat horisontellt så att layout(knapparna) och canvaslayout(grafen) placeras bredvid varandra
window.setLayout(QHBoxLayout())
canvasLayout = QVBoxLayout()
layout = QVBoxLayout()

button = QPushButton('Open File')
combo = QComboBox()
button.setFixedWidth(120)
combo.setFixedWidth(120)
groupCombo = QComboBox()
groupCombo.setFixedWidth(120)

#anropar variablerna utanför funktionen som global för att de inte ska ignoreras i funktionen
#föregående grafen tas bort och ersätts om det inte är första gången man väljer ett item
previousGraph = "None"
hasChosen = False
def addCanvas():
   global previousGraph
   global hasChosen
   global groupItems
   if hasChosen:
        canvasLayout.removeWidget(previousGraph)

   currentItem = str(combo.currentText())
   currentGroup = str(groupCombo.currentText())
   itemData = (readData(path, currentGroup, currentItem))

   graph = plot(itemData)
   canvasLayout.addWidget(graph, alignment=Qt.AlignRight | Qt.AlignCenter)

   previousGraph = graph
   hasChosen = True

def chooseFile():
    global path
    
    #eftersom QFileDialog returnar (path, settings) och inte bara path så anges index 0 för att specifiera första värdet
    path = QFileDialog.getOpenFileName(None, "Open a h5 log file", "", "h5 files (*.h5*)")[0]

    #efter att ny fil har valts måste combobox rensas och uppdateras, annars blir gamla items kvar
    groupCombo.clear()
    combo.clear()
    try:
        allGroups = retrieveGroups(path)
        for group in allGroups:
            groupCombo.addItem(group)

    except:
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("You need to choose a file")
        msg.exec_()

def chooseItem():
    global path
    combo.clear()
    chosenGroup = groupCombo.currentIndex()
    group = retrieveGroups(path)[chosenGroup]
    datasets = groupStructure(path, group)
    for dataset in datasets:
        combo.addItem(dataset)

button.clicked.connect(chooseFile)
combo.activated.connect(addCanvas)
groupCombo.activated.connect(chooseItem)

layout.addWidget(button, alignment=Qt.AlignLeft)
layout.addWidget(combo, alignment=Qt.AlignLeft | Qt.AlignTop)
layout.addWidget(groupCombo, alignment=Qt.AlignLeft | Qt.AlignTop)
window.layout().addLayout(layout)
window.layout().addLayout(canvasLayout)
window.show()
app.exec()


