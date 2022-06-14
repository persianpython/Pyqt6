from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont, QPainter, QPen
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(200, 200, 700, 400)
        self.setMouseTracking(True)
        vbox = QVBoxLayout()
        self.label_press = QLabel('Press :')
        self.label_press.setFont(QFont('arial', 20))
        self.label_release = QLabel('Release : ')
        self.label_release.setFont(QFont('arial', 20))
        vbox.addWidget(self.label_press)
        vbox.addWidget(self.label_release)
        self.setLayout(vbox)
        self.pos = [0, 0]

    # def mouseMoveEvent(self, event):
    #     x, y = event.pos().x(), event.pos().y()
    #     self.label.setText(f"X: {x} y: {y}")
    #     self.update()
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(Qt.GlobalColor.red, 15))
        painter.drawPoint(self.pos[0], self.pos[1])
        painter.end()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.label_press.setText(f"Press : {event.pos().x()}")
            self.pos[0], self.pos[1] = event.pos().x(), event.pos().y()
            self.update()

    def mouseReleaseEvent(self, event):
        self.label_release.setText(f"Release : {event.pos().x()}")


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
