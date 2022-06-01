from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QFontDialog,\
    QColorDialog
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt6.QtCore import QFileInfo, Qt
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
        self.actionRight.triggered.connect(self.right)
        self.actionLeft.triggered.connect(self.left)
        self.actionJustify.triggered.connect(self.justify)
        self.actionCenter.triggered.connect(self.center)
        self.actionFont.triggered.connect(self.set_font)
        self.actionColor.triggered.connect(self.set_color)


        self.actionAbout_Us.triggered.connect(self.about)

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

    def left(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def right(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight)

    def center(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def justify(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify)

    def set_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def set_color(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def about(self):
        QMessageBox.about(self, 'About App', 'In Avalin Proje Takmili Amozesh Pyqt6 hastesh')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = NotepadMain()
    sys.exit(app.exec())
