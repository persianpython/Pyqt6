# pip install pyqt6
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
import sys
from PyQt6.QtGui import QIcon

app = QApplication(sys.argv)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.menuBar().addMenu('File')
        # self.statusBar().showMessage("Salam")
        # self.setMaximumSize(500, 700)
        # self.setMinimumSize(100, 100)
        self.setFixedWidth(500)
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))

window = MyWindow()

window.show()

sys.exit(app.exec())

# pip install pyqt6-tools
# pip install pyqt5-tools

# python/lib/pyqt6/bin/designer.exe
