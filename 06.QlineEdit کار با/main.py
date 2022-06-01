from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMenu, QLineEdit
import sys
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtCore import QSize

app = QApplication(sys.argv)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))

        self.label = QLabel("", self)
        self.label.setGeometry(100, 200, 50, 50)

        self.button = QPushButton('QPushButton', self)
        self.button.setGeometry(200, 0, 100, 50)
        self.button.setFont(QFont('Arial', 7, QFont.Weight.ExtraBold))
        self.button.setIcon(QIcon('logo.png'))
        self.button.setIconSize(QSize(50, 50))
        self.button.clicked.connect(self.clicked)

        self.create_qline_edit()

    def create_qline_edit(self):
        self.input_text = QLineEdit(self)
        self.input_text.setGeometry(5, 5, 150, 50)
        # self.input_text.setText('Default Text !')
        self.input_text.setPlaceholderText('Enter username')
        self.input_text.setFont(QFont('Arial', 10, QFont.Weight.ExtraBold))
        self.input_text.setStyleSheet('color:blue')
        self.input_text.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

    def clicked(self):
        if self.input_text.text():
            self.label.setText(self.input_text.text())
            self.input_text.clear()

window = MyWindow()

window.show()

sys.exit(app.exec())
