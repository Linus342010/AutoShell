from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow
from PyQt5.QtCore import QSize
import sys

def clicked():
    print("Button was clicked!")

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Drag & Drop Builder")
window.setFixedSize(QSize(800,400))
window.show()

button = QPushButton("Click me")
button.setFixedSize(QSize(100,50))
button.setAcceptDrops(True)
button.clicked.connect(clicked)
button.show()

window.setCentralWidget(button)

app.exec()