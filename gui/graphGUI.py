from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


def selectedItem(item):
    print(item)

app = QApplication([])
app.setStyle("Fusion")

window = QWidget()
layout = QVBoxLayout()

combo = QComboBox()
combo.addItem("Signal 1")
combo.addItem("Signal 2")
combo.addItem("Signal 3")
combo.activated[str].connect(selectedItem) 
layout.addWidget(combo)

fig = Figure(figsize=(4, 5), dpi=100)
axes = fig.add_subplot(111)
axes.plot([0,1,2,3,4], [10,1,20,3,40])

canvas = FigureCanvasQTAgg(fig) 
layout.addWidget(canvas)


window.setLayout(layout)
window.show()
app.exec()

