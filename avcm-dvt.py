import h5py
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox, QFileDialog
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
window.setFixedWidth(600)
window.setFixedHeight(350)
layout = QVBoxLayout()
button = QPushButton('Open File')
combo = QComboBox()

path = "log_210129_124838_1611920928.h5"

firstGroup = retrieveGroups(path)[0]
groupItems = groupStructure(path, firstGroup)
for item in groupItems:
    combo.addItem(item)

 
#anropar variablerna utanför funktionen som global för att de inte ska ignoreras i funktionen
previousGraph = "None"
hasChosen = False
def addCanvas():
   global previousGraph
   global hasChosen
   if hasChosen:
        layout.removeWidget(previousGraph)

   currentItem = str(combo.currentText())
   itemData = (readData(path, firstGroup, currentItem))
   graph = plot(itemData)
   layout.addWidget(graph)
   previousGraph = graph
   hasChosen = True

def chooseFile():
    global path
    
    #eftersom QFileDialog returnar (path, settings) och inte bara path så anges index 0 för att specifiera första värdet
    path = QFileDialog.getOpenFileName(None, "Open a h5 log file", "", "h5 files (*.h5*)")[0]

    #efter att ny fil har valts måste combobox rensas och uppdateras, annars blir gamla items kvar
    combo.clear()
    firstGroup = retrieveGroups(path)[0]
    groupItems = groupStructure(path, firstGroup)
    for item in groupItems:
      combo.addItem(item)


button.clicked.connect(chooseFile)
combo.activated.connect(addCanvas)
layout.addWidget(button)
layout.addWidget(combo)

window.setLayout(layout)
window.show()
app.exec()


