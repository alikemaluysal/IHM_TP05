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
		open_action.triggered.connect(self.openFile)

		save_action = QAction(QIcon("save.png"), "Save", self)
		save_action.setShortcut("Ctrl+S")
		save_action.setStatusTip("Save")
		save_action.triggered.connect(self.saveFile)

		copy_action = QAction(QIcon("copy.png"), "Copy", self)
		copy_action.setShortcut("Ctrl+C")
		copy_action.setStatusTip("Copy")

		quit_action = QAction(QIcon("quit.png"), "Quit", self)
		quit_action.setShortcut("Ctrl+Q")
		quit_action.setStatusTip("Quit")
		quit_action.triggered.connect(self.quitApp)


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


	def openFile(self):
		options = QFileDialog.Options()
		file_name, _ = QFileDialog.getOpenFileName(
			self,
			"Open File",
			"",
			"All Files (*);;Text Files (*.txt)",
			options=options
		)
		if file_name:
			print(f"Selected file: {file_name}")

	def saveFile(self):
		options = QFileDialog.Options()
		file_name, _ = QFileDialog.getSaveFileName(
			self,
			"Save File",
			"",
			"All Files (*);;Text Files (*.txt)",
			options=options
		)
		if file_name:
			print(f"File to save: {file_name}")


	def quitApp(self):
		print("quit app")
		self.close()


	


def main(args):
    # print("Arguments reçus :", args)

	app = QApplication(args)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_()) 

	

if __name__ == "__main__":
    main(sys.argv)
