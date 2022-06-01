# pip install pyqt6
from PyQt6.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
from PyQt6.QtGui import QIcon
import sys

app = QApplication(sys.argv)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()



window = MyWindow()

window.show()

sys.exit(app.exec())
