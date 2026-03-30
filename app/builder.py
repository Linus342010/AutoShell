from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout, QListWidgetItem, QMainWindow
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ListWidgetLeft = QListWidget()
        self.ListWidgetRight = QListWidget()

        self.ListWidgetLeft.setAcceptDrops(True)
        self.ListWidgetLeft.setDragEnabled(True)
        self.ListWidgetRight.setAcceptDrops(True)
        self.ListWidgetRight.setDragEnabled(True)

        self.setGeometry(300, 350, 800, 400)

        self.hboxlayout = QHBoxLayout()
        self.hboxlayout.addWidget(self.ListWidgetLeft)
        self.hboxlayout.addWidget(self.ListWidgetRight)

        l1 = QListWidgetItem("Command 1")
        l2 = QListWidgetItem("Command 2")

        self.ListWidgetLeft.insertItem(1, l1)
        self.ListWidgetLeft.insertItem(2, l2)


        self.setWindowTitle("AutoShell Drag&Drop Builder")
        self.setLayout(self.hboxlayout)
        self.show()
        
app = QApplication(sys.argv)
builder = window()
app.exec()

