from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QSlider, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt


import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setMinimum(10)
        self.slider.setMaximum(20)
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider.setTickInterval(2)
        self.slider.valueChanged.connect(self.slider_changed)

        self.hbox = QHBoxLayout()

        self.lable = QLabel('')

        self.hbox.addWidget(self.slider)
        self.hbox.addWidget(self.lable)
        self.setLayout(self.hbox)

    def slider_changed(self):
        value = self.slider.value()
        self.lable.setText(str(value))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())