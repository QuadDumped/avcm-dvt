import h5py
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox
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
combo = QComboBox()

firstGroup = retrieveGroups()[0]
groupItems = groupStructure(firstGroup)
for item in groupItems:
    combo.addItem(item)



#anropar variablerna utanför funktionen som global för att de inte ska skrivas över i funktionen
#
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



combo.currentIndexChanged.connect(addCanvas)
layout.addWidget(combo)

window.setLayout(layout)
window.show()
app.exec()
