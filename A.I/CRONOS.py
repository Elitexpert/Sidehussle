# importing the required libraries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		
		# string value
		title = "Title of window"

		# set the title
		self.setWindowTitle(title)

		# setting the geometry of window
		self.setGeometry(0, 0, 500, 300)

		# show all the widgets
		self.show()

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
