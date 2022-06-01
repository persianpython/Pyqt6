from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QComboBox
from PyQt6.QtGui import QIcon, QFont


import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))

        self.combo = QComboBox()

        # self.combo.setGeometry(x, y, w, h)
        self.combo.addItems(['salam', 'khobi', 'test'])
        self.combo.setFont(QFont('arial', 20))

        self.combo.currentIndexChanged.connect(self.change_combo)

        hbox = QHBoxLayout()
        hbox.addWidget(self.combo)
        self.setLayout(hbox)

    def change_combo(self):
        print(self.combo.currentText())
        print(self.combo.currentIndex())
        self.combo.setCurrentIndex(0)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())