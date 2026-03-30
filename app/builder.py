from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout, QListWidgetItem, QMainWindow
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ListWidgetLeft = QListWidget()
        self.ListWidgetRight = QListWidget()

        self.ListWidgetLeft(True)
        self.ListWidgetRight(True)

