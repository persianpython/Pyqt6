from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt6.QtCore import QFileInfo
from PyQt6.QtGui import QFont
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
        self.actionPrint.triggered.connect(self.print_file)
        self.actionPrint_Preview.triggered.connect(self.preview_dialog)
        self.actionExport_PDF.triggered.connect(self.export_pdf)

        self.actionQuite.triggered.connect(self.close_program)


        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionPaste.triggered.connect(self.textEdit.paste)
        self.actionCut.triggered.connect(self.textEdit.cut)

        self.actionBold.triggered.connect(self.set_bold)
        self.actionUnderLine.triggered.connect(self.set_underline)
        self.actionItalic.triggered.connect(self.set_italic)

    def set_bold(self):
        font = QFont()
        font.setBold(True)
        self.textEdit.setFont(font)

    def set_italic(self):
        font = QFont()
        font.setItalic(True)
        self.textEdit.setFont(font)

    def set_underline(self):
        font = QFont()
        font.setUnderline(True)
        self.textEdit.setFont(font)

    def close_program(self):
        self.close()

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

    def print_file(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer)

        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.textEdit.print(printer)

    def preview_dialog(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintPreviewDialog(printer, self)

        dialog.paintRequested.connect(self.preview_file)
        dialog.exec()

    def preview_file(self, printer):
        self.textEdit.print(printer)

    def export_pdf(self):
        fn, _ = QFileDialog.getSaveFileName(self, 'Export PDF', 'output.pdf')
        if fn:
            if QFileInfo(fn).suffix() == "": fn = f'{fn}.pdf'
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print(printer)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = NotepadMain()
    sys.exit(app.exec())
