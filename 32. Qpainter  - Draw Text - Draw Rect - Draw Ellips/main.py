from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush, QTextDocument
from PyQt6.QtCore import Qt, QRect, QRectF
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
        # painter.drawText(100, 100, 'Persian Python')
        # rect = QRect(100, 100, 100, 70)
        # painter.drawRect(rect)
        # painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, "Persian Python")
        document = QTextDocument(self)
        rect = QRectF(0, 0, 100, 200)
        document.setTextWidth(rect.width())
        document.setHtml("<font size=20 color=red><b> Test !!! </b></font>")
        document.drawContents(painter, rect)

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
