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

		self.textEdit = QTextEdit()
		self.setCentralWidget(self.textEdit)

		self.statusBar().showMessage("Ready")

		open_action.triggered.connect(self.openFile)
		save_action.triggered.connect(self.saveFile)
		quit_action.triggered.connect(self.quitApp)




	def openFile(self):
		options = QFileDialog.Options()
		file_name, _ = QFileDialog.getOpenFileName(
			self,
			"Open File",
			"",
			"HTML Files (*.html *.htm);;All Files (*)",
			options=options
		)
		if file_name:
			try:
				with open(file_name, "r", encoding="utf-8") as file:
					content = file.read()
					self.textEdit.setHtml(content)
					print(f"Loaded file: {file_name}")
			except Exception as e:
				print(f"Error loading file: {e}")

	def saveFile(self):
		options = QFileDialog.Options()
		file_name, _ = QFileDialog.getSaveFileName(
			self,
			"Save File",
			"",
			"HTML Files (*.html *.htm);;All Files (*)",
			options=options
		)
		if file_name:
			try:
				with open(file_name, "w", encoding="utf-8") as file:
					content = self.textEdit.toHtml()
					file.write(content)
					print(f"Saved file: {file_name}")
			except Exception as e:
				print(f"Error saving file: {e}")


	def quitApp(self):
		result = self.confirmExit()
		if result:
			sys.exit()


	def confirmExit(self):
		reply = QMessageBox.question(
			self,
			"Confirm Exit",
			"Are you sure you want to exit?",
			QMessageBox.Yes | QMessageBox.No,
			QMessageBox.No
		)
		if reply == QMessageBox.Yes:
			print("Exiting application...")
			return True
		else:
			print("Exit canceled.")
			return False
		


	


def main(args):
    # print("Arguments reçus :", args)

	app = QApplication(args)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_()) 

	

if __name__ == "__main__":
    main(sys.argv)
