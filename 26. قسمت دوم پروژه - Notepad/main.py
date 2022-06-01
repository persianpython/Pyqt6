from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from Notepad import Ui_MainWindow
import sys


class NotepadMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.actionSave.triggered.connect(self.save_file)

    def save_file(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')
        if filename[0]:
            with open(filename[0], 'w') as file:
                text = self.textEdit.toPlainText()
                file.write(text)
                QMessageBox.about(self, 'Save File', 'file save shod !')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = NotepadMain()
    sys.exit(app.exec())
