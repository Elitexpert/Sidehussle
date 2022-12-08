# importing the required libraries

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
	def __init__(self):
		super().__init__()


		# set the title
		self.setWindowTitle("Cronos")

		# setting the geometry of window
		self.setGeometry(60, 60, 600, 400)


		# creating a window background
		label = QLabel(self)
		pixmap = QPixmap('C:\Users\alter\OneDrive\Documents\Sidehussle\project0\Images\499419.jpg')
		label.setPixmap(pixmap)


		# show all the widgets
		self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()
# start the app
sys.exit(App.exec())

