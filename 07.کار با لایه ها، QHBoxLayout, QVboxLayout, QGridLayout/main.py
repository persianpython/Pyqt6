from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
import sys
from PyQt6.QtGui import QIcon

app = QApplication(sys.argv)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))
        self.create_widgets()

    def create_widgets(self):
        btn1 = QPushButton('btn1')
        btn2 = QPushButton('btn2')
        btn3 = QPushButton('btn3')
        btn4 = QPushButton('btn4')

        grid = QGridLayout()

        grid.addWidget(btn1, 0 ,0)
        grid.addWidget(btn2, 1 ,0)
        grid.addWidget(btn3, 1 ,1)
        grid.addWidget(btn4, 1 ,2)


        # vbox = Q()
        # vbox.addWidget(btn1)
        # vbox.addWidget(btn2)
        # vbox.addWidget(btn3)
        # vbox.addWidget(btn4)
        # vbox.addSpacing(100)
        # # vbox.setStretch(1, 1)
        self.setLayout(grid)



window = MyWindow()

window.show()

sys.exit(app.exec())
