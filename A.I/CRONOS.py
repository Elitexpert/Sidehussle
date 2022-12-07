#imports
import PyQt6
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

#window
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
app = QApplication(sys.argv)
window = QWidget()
window.show() 
app.exec()
title = "Cronos"
self.setWindowTitle(title)
self.show()
