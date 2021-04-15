from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class CloseButton(QWidget):
    def __init__(self, widget, isCompareGraph = True, axes = None, axesTitle = None):
        super(CloseButton, self).__init__()
        self.button = QPushButton("Close")
        self.widget = widget
        self.isCompareGraph = isCompareGraph
        self.axes = axes
        self.axesTitle = axesTitle
        self.button.clicked.connect(self.onClick)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def onClick(self):
        self.widget.setParent(None)
        self.button.setParent(None)
        #Clearar axes och axestitle om knappen tillhör en graf som inte är compare, detta måste göras då axes och axesTitle är globala
        if(self.isCompareGraph == False):
            self.axes.clear()
            self.axesTitle.clear()


    
class GridWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(1080)
        self.setFixedWidth(1920)

    def pushLayout(self, layout):
        self.setLayout(layout)




        

      

  


      

   


