from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget
from PyQt6.QtGui import QIcon, QFont


import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(200,200, 700, 300)

        self.vbox = QVBoxLayout()
        self.list_widget = QListWidget()
        self.list_widget.insertItem(0, 'first')
        self.list_widget.insertItem(1, 'second')
        self.list_widget.insertItem(2, 'third')
        self.list_widget.setFont(QFont('arial', 25))
        # self.list_widget.setStyleSheet('background-color:red')
        # print(self.list_widget.count())
        self.list_widget.currentTextChanged.connect(self.list_widget_changed)

        self.list_widget.takeItem(1)

        self.vbox.addWidget(self.list_widget)
        self.setLayout(self.vbox)

    def list_widget_changed(self):
        print(self.list_widget.currentItem().text())

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())