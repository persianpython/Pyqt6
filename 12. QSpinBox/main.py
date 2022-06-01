from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpinBox, QLineEdit
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

        lable = QLabel('قیمت کالا')

        self.price = QLineEdit()
        self.price.setText(f"{3000}")
        self.price.setDisabled(True)

        hbox.addWidget(lable)
        hbox.addWidget(self.price)

        self.spin = QSpinBox()
        self.spin.setMinimum(0)
        self.spin.setMaximum(5)

        # event change value
        # self.spin.valueChanged.connect(self.change_value_spin)
        # event focus out
        self.spin.editingFinished.connect(self.change_value_spin)

        self.total_price = QLineEdit()

        hbox.addWidget(self.spin)

        hbox.addWidget(self.total_price)


        self.setLayout(hbox)

    def change_value_spin(self):
        if self.spin.value():
            total_price = int(self.price.text()) * self.spin.value()
            self.total_price.setText(str(total_price))

        else:
            self.total_price.setText("0")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())