import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.windowTitle = "Main Window"

		menuBar = self.menuBar()
		file_menu = menuBar.addMenu("File")


		open_action = QAction(QIcon("open.png"), "Open", self)
		open_action.setShortcut("Ctrl+O")
		open_action.setStatusTip("Open")

		save_action = QAction(QIcon("save.png"), "Save", self)
		save_action.setShortcut("Ctrl+S")
		save_action.setStatusTip("Save")

		copy_action = QAction(QIcon("copy.png"), "Copy", self)
		copy_action.setShortcut("Ctrl+C")
		copy_action.setStatusTip("Copy")

		quit_action = QAction(QIcon("quit.png"), "Quit", self)
		quit_action.setShortcut("Ctrl+Q")
		quit_action.setStatusTip("Quit")
		quit_action.triggered.connect(self.close)


		file_menu.addAction(open_action)
		file_menu.addAction(save_action)
		file_menu.addAction(copy_action)
		file_menu.addAction(quit_action)

		toolbar = QToolBar("Toolbar")
		self.addToolBar(toolbar)
		toolbar.addAction(open_action)
		toolbar.addAction(save_action)
		toolbar.addAction(copy_action)
		toolbar.addAction(quit_action)


		textEdit = QTextEdit()
		self.setCentralWidget(textEdit)

		self.statusBar().showMessage("Ready")
	


def main(args):
    # print("Arguments reçus :", args)

	app = QApplication(args)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_()) 

	

if __name__ == "__main__":
    main(sys.argv)
