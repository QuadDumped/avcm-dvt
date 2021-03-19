from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication([])
app.setStyle("Fusion")

window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton("Button"))
window.setLayout(layout)

window.show()
app.exec()

