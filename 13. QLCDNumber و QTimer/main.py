from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLCDNumber
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTime, QTimer

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))

        self.lcd = QLCDNumber()

        self.lcd.setStyleSheet('background:red')

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.lcd)

        self.setLayout(self.hbox)

        self.show_time()

        self.timer = QTimer(self)

        self.timer.timeout.connect(self.show_time)

        self.timer.start(1000)
        self.timer.stop()


    def show_time(self):
        time = QTime.currentTime()
        show_time = time.toString('mm:ss')
        self.lcd.display(show_time)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())