from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from Notepad import Ui_MainWindow
import sys


class NotepadMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.actionSave.triggered.connect(self.save_file)
        self.actionNew.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_file)

    def save_file(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')
        if filename[0]:
            with open(filename[0], 'w') as file:
                text = self.textEdit.toPlainText()
                file.write(text)
                QMessageBox.about(self, 'Save File', 'file save shod !')

    def maybe_save(self):
        if not self.textEdit.document().isModified():
            return True

        result = QMessageBox.warning(self, 'Notepad', 'matn eslah shode ast mikhahid save shavad ?',
                                     QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Cancel)
        if result == QMessageBox.StandardButton.Save:
            self.save_file()
        elif result == QMessageBox.StandardButton.Cancel:
            return False

        return True

    def new_file(self):
        if self.maybe_save():
            self.textEdit.clear()

    def open_file(self):
        if not self.maybe_save():
            return
        name_file = QFileDialog.getOpenFileName(self, 'Open File')
        print(name_file)
        if name_file[0]:
            with open(name_file[0], 'r') as file:
                self.textEdit.setText(file.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = NotepadMain()
    sys.exit(app.exec())
