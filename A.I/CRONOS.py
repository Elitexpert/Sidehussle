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
title = "Cronos"
 
        # set the title
self.setWindowTitle(title)
 
        # setting  the geometry of window
self.setGeometry(0, 0, 500, 300)
 
        # show all the widgets
self.show()
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())