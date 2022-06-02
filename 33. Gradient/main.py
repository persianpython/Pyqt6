from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush, QConicalGradient
from PyQt6.QtCore import Qt
import sys
import time


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(200, 200, 700, 400)
        vbox = QVBoxLayout()
        self.setLayout(vbox)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 5, Qt.PenStyle.SolidLine))

        grad1 = QConicalGradient(100, 100, 0)
        grad1.setColorAt(0.0, Qt.GlobalColor.red)
        grad1.setColorAt(0.5, Qt.GlobalColor.blue)
        grad1.setColorAt(0.9, Qt.GlobalColor.yellow)

        painter.setBrush(grad1)
        painter.drawRect(10, 10, 200, 200)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
