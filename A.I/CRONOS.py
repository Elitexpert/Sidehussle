# importing the required libraries

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import *
from time import *


class App(QWidget):
	def __init__(self):
		super().__init__()
		self.Title = 'Cronos'
		self.left = 10
		self.top = 10
		self.width = 640
		self.height = 480
		self.initUI()


	def initUI(self):
		self.setWindowTitle(self.Title)
		self.setGeometry(self.left, self.top, self.width, self.height)


		# creating a window
		label = QLabel(self)
		pixmap = QPixmap(r'C:\Users\alter\OneDrive\Documents\Sidehussle\project0\Images\499419.jpg')
		label.setPixmap(pixmap)
		self.resize(pixmap.width(),pixmap.height())
		self.show()

		#create animations
		Line_1="Hello im Cronos"
		Line_2="Im Sidehussle little buddy"
		Line_3="I heard your looking for a job"
		line_4=""


# create pyqt5 app
if __name__=='__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
