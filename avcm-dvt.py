import h5py
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from gui.graphGUI import createCanvas, selectedItem
from customwidgets import CloseButton, GridWindow
from h5reader import groupStructure, retrieveGroups, groupItem, readData

app = QApplication([])
app.setStyle("Fusion")

window = QWidget()
window.setWindowTitle("Autonomous Vehicle Controle Module Data Visualization Tool")
window.setFixedWidth(1280)
window.setFixedHeight(900) 

#window är strukturerat horisontellt så att layout(knapparna) och canvaslayout() placeras bredvid varandra
window.setLayout(QHBoxLayout())
canvasLayout = QVBoxLayout()
buttonLayout = QVBoxLayout()
graphButtonLayout = QHBoxLayout()

buttonLayout.setContentsMargins(0,0,0,700)

button = QPushButton('Open File')
grid = GridWindow()
combo = QComboBox()
compareCheck = QCheckBox("Compare")
groupCombo = QComboBox()
button2 = QPushButton("Clear")
popoutButton = QPushButton("Popout")
gridButton = QPushButton("Grid")

button.setFixedWidth(120)
combo.setFixedWidth(120)
groupCombo.setFixedWidth(120)
button2.setFixedWidth(120)
popoutButton.setFixedWidth(120)
gridButton.setFixedWidth(120)
  
fig = Figure(figsize=(12, 12), dpi=100)
axes = fig.add_subplot(111)
axesTitle = []
plots = []

#anropar variablerna utanför funktionen som global för att de inte ska ignoreras i funktionen
#föregående grafen tas bort och ersätts om det inte är första gången man väljer ett item
previousGraph = "None"
hasChosen = False
compare = False


def popOut():
    try:
        currentItem = str(combo.currentText())
        currentGroup = str(groupCombo.currentText())
        itemData = (readData(path, currentGroup, currentItem))

    except:
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("You need to choose a file")
        msg.exec_()
        return()

    x = []
    y = []
    i = 0

    for row in itemData:
       i+=1
       x.append(i)
       y.append(row[1])

    plt.figure()
    plt.plot(x, y) 
    plt.title(currentGroup + "/" + currentItem)

    plt.show()

def compareClicked(): 
   global compare 
   compare = compareCheck.isChecked()
  
def clearPlot():
    global axes
    axes.clear()
    axesTitle.clear()

    #axes.lines.pop(0)

    #tar bort alla widgets i canvaslayout
    for i in reversed(range(canvasLayout.count())): 
     canvasLayout.itemAt(i).widget().setParent(None)


def chooseItem():
   global previousGraph
   global hasChosen
   global axes

   if compare == False:
        if hasChosen:
         for i in reversed(range(canvasLayout.count())): 
              canvasLayout.itemAt(i).widget().setParent(None) 
  
   currentItem = str(combo.currentText())
   currentGroup = str(groupCombo.currentText())
   itemData = (readData(path, currentGroup, currentItem))

   x = []
   y = []
   i = 0

   for row in itemData:
       i+=1
       x.append(i)
       y.append(row[1])

   graph = createCanvas(fig)
   windowHeight = window.height() 
   #graferna placeras jämnt inom fönstret
   fig.set_figheight(windowHeight)

   if compare == False:
        axes.plot(x, y)
        if currentItem not in axesTitle:
            axesTitle.append(currentItem)    
        axes.set_title(axesTitle)

        closeButton = CloseButton(graph, False, axes, axesTitle)
        
        canvasLayout.addWidget(closeButton, alignment=Qt.AlignRight | Qt.AlignCenter)
        canvasLayout.addWidget(graph, alignment=Qt.AlignRight | Qt.AlignCenter)

   else:
        #definierar en ny figure så att man inte plottar till den globala
        fig2 = Figure(figsize=(12, windowHeight), dpi=100)
        axes2 = fig2.add_subplot(111)
        graph2 = createCanvas(fig2)     
        axes2.plot(x, y)
        axes2.set_title(currentItem)

        closeButton = CloseButton(graph2)
            
        canvasLayout.addWidget(closeButton, alignment=Qt.AlignRight | Qt.AlignCenter)
        canvasLayout.addWidget(graph2, alignment=Qt.AlignRight | Qt.AlignCenter)

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

def chooseGroup():
    global path
    combo.clear()
    chosenGroup = groupCombo.currentIndex()
    group = retrieveGroups(path)[chosenGroup]
    datasets = groupStructure(path, group)
    for dataset in datasets:
        combo.addItem(dataset)


def createGrid():

    try:
        currentGroup = str(groupCombo.currentText())
        dataSets = groupStructure(path, currentGroup)

    except: 
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("You need to choose a file")
        msg.exec_()
        return()


    gridlayout = QGridLayout()
    gridlayout.setColumnStretch(4, 6)

    for dataset in dataSets:

        fig = Figure(figsize=(12, 10), dpi=100)
        axes = fig.add_subplot(111)

        itemData = (readData(path, currentGroup, dataset))

        x = []
        y = []
        i = 0

        for row in itemData:
          i+=1
          x.append(i)
          y.append(row[1])

        graph = createCanvas(fig)
        axes.plot(x, y)
        axes.set_title(dataset)
        graph.setMaximumHeight(450)
        graph.setMaximumWidth(700)
        gridlayout.addWidget(graph)

    grid.pushLayout(gridlayout)
    grid.setStyleSheet("background-color:white;")
    grid.show()


button.clicked.connect(chooseFile)
combo.activated.connect(chooseItem)
groupCombo.activated.connect(chooseGroup)
button2.clicked.connect(clearPlot)
compareCheck.clicked.connect(compareClicked)
popoutButton.clicked.connect(popOut)
gridButton.clicked.connect(createGrid)
buttonLayout.addWidget(button, alignment=Qt.AlignLeft | Qt.AlignTop)
buttonLayout.addWidget(groupCombo, alignment=Qt.AlignLeft | Qt.AlignTop)
buttonLayout.addWidget(combo, alignment=Qt.AlignLeft | Qt.AlignTop)
buttonLayout.addWidget(compareCheck, alignment=Qt.AlignLeft | Qt.AlignTop)
buttonLayout.addWidget(button2, alignment=Qt.AlignLeft | Qt.AlignTop)
buttonLayout.addWidget(popoutButton, alignment=Qt.AlignLeft | Qt.AlignTop)
buttonLayout.addWidget(gridButton, alignment=Qt.AlignLeft | Qt.AlignTop)
window.layout().addLayout(buttonLayout)
window.layout().addLayout(canvasLayout)

window.show()
app.exec()


