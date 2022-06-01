from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont


import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(200,200, 700, 300)

        mylist = [
            ['porteghal', '20.000', '100'],['sib', '15.000', '500']
        ]

        vbox = QVBoxLayout()

        table = QTableWidget()
        table.setFont(QFont('arial', 20))
        table.setColumnCount(3)
        table.setRowCount(3)
        table.setItem(0, 0, QTableWidgetItem('میوه'))
        table.setItem(0, 1, QTableWidgetItem('قیمت'))
        table.setItem(0, 2, QTableWidgetItem('موجودی'))

        for i, item in enumerate(mylist):
            for j, _item in enumerate(item):
                table.setItem(i+1, j, QTableWidgetItem(_item))

        vbox.addWidget(table)
        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())