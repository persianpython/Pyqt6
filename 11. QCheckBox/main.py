from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox, QRadioButton, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))
        self.create_widgets()

    def create_widgets(self):
        hbox = QHBoxLayout()
        rad1 = QCheckBox('Python')
        rad1.setIcon(QIcon('images/python.png'))
        rad1.setIconSize(QSize(40,40))
        rad1.setFont(QFont('Arial', 15))
        rad1.setChecked(True)
        rad1.stateChanged.connect(self.radio_selected)

        hbox.addWidget(rad1)

        rad2 = QCheckBox('Java')
        rad2.setIcon(QIcon('images/java.png'))
        rad2.setIconSize(QSize(40,40))
        rad2.setFont(QFont('Arial', 15))
        rad2.stateChanged.connect(self.radio_selected)

        hbox.addWidget(rad2)

        rad3 = QCheckBox('JavaScript')
        rad3.setIcon(QIcon('images/javascript.png'))
        rad3.setIconSize(QSize(40,40))
        rad3.setFont(QFont('Arial', 15))
        rad3.stateChanged.connect(self.radio_selected)

        hbox.addWidget(rad3)

        vbox = QVBoxLayout()
        self.lable = QLabel()
        vbox.addWidget(self.lable)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            print(radio_btn.text())
            self.lable.setText(radio_btn.text())
        print(radio_btn.text())


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())