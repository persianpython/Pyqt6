from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon


import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(200,200, 700, 300)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())