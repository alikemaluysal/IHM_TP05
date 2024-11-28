import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QToolBar, QFileDialog, QMessageBox
)
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar().showMessage("Ready")

        # Initialize UI components
        self.setupMenuBar()
        self.setupToolBar()

    def setupMenuBar(self):
        """Create the menu bar and its actions."""
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        self.open_action = self.createAction(
            "Open", "Ctrl+O", "Open a file", "open.png", self.openFile
        )
        self.save_action = self.createAction(
            "Save", "Ctrl+S", "Save a file", "save.png", self.saveFile
        )
        self.copy_action = self.createAction(
            "Copy", "Ctrl+C", "Copy selected text", "copy.png", self.copyText
        )
        self.quit_action = self.createAction(
            "Quit", "Ctrl+Q", "Exit the application", "quit.png", self.quitApp
        )

        file_menu.addActions([self.open_action, self.save_action, self.copy_action, self.quit_action])

    def setupToolBar(self):
        """Create the toolbar and add actions."""
        toolbar = QToolBar("Toolbar")
        self.addToolBar(toolbar)
        toolbar.addActions([self.open_action, self.save_action, self.copy_action, self.quit_action])

    def createAction(self, name, shortcut, status_tip, icon, handler=None):
        """Helper to create and configure an action."""
        action = QAction(QIcon(icon), name, self)
        action.setShortcut(shortcut)
        action.setStatusTip(status_tip)
        if handler:
            action.triggered.connect(handler)
        return action

    def openFile(self):
        """Open a file and display its content."""
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "HTML Files (*.html *.htm);;All Files (*)"
        )
        if file_name:
            try:
                with open(file_name, "r", encoding="utf-8") as file:
                    self.textEdit.setHtml(file.read())
                self.statusBar().showMessage(f"File loaded: {file_name}")
            except Exception as e:
                self.showError(f"Error loading file: {e}")

    def saveFile(self):
        """Save the current content to a file."""
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "",
            "HTML Files (*.html *.htm);;All Files (*)"
        )
        if file_name:
            try:
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(self.textEdit.toHtml())
                self.statusBar().showMessage(f"File saved: {file_name}")
            except Exception as e:
                self.showError(f"Error saving file: {e}")

    def copyText(self):
        """Copy selected text from the text editor."""
        cursor = self.textEdit.textCursor()
        selected_text = cursor.selectedText()
        if selected_text:
            QApplication.clipboard().setText(selected_text)
            self.statusBar().showMessage("Text copied to clipboard")
        else:
            self.statusBar().showMessage("No text selected")

    def quitApp(self):
        """Handle the Quit action."""
        if self.confirmExit():
            self.close()

    def closeEvent(self, event):
        """Intercept the window close event for confirmation."""
        if self.confirmExit():
            event.accept()
        else:
            event.ignore()

    def confirmExit(self):
        """Display a confirmation dialog before exiting."""
        reply = QMessageBox.question(
            self,
            "Confirm Exit",
            "Are you sure you want to exit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        return reply == QMessageBox.Yes

    def showError(self, message):
        """Display an error message dialog."""
        QMessageBox.critical(self, "Error", message)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
