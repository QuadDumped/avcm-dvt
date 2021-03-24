import h5py
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
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


path = ""

firstGroup = retrieveGroups()[0]
groupItems = groupStructure(firstGroup)
for item in groupItems:
    combo.addItem(item)


#anropar variablerna utanför funktionen som global för att de inte ska skrivas över i funktionen


previousGraph = "None"
hasChosen = False
def addCanvas():
   global previousGraph
   global hasChosen

   if hasChosen:
        layout.removeWidget(previousGraph)

   currentItem = str(combo.currentText())
   itemData = (readData(firstGroup, currentItem))
   graph = plot(itemData)
   layout.addWidget(graph)
   previousGraph = graph
   hasChosen = True

def chooseFile():
    global path
    path = QFileDialog()
    path.setNameFilters(["log files h5 (*.h5)"])
    path.exec_()



button.clicked.connect(chooseFile)
combo.currentIndexChanged.connect(addCanvas)
layout.addWidget(button)
layout.addWidget(combo)

window.setLayout(layout)
window.show()
app.exec()
