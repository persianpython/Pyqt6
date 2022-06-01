from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtWidgets import QInputDialog
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(200,200, 700, 300)
        vbox = QHBoxLayout()

        #
        self.label = QLabel('Get Input : ')
        self.label.setFont(QFont('arial', 26))
        vbox.addWidget(self.label)
        #
        self.line_edit = QLineEdit()
        self.line_edit.setFont(QFont('arial', 26))
        vbox.addWidget(self.line_edit)

        #
        self.push_button = QPushButton('Get Input !')
        self.push_button.setFont(QFont('arial', 26))
        self.push_button.clicked.connect(self.get_text)
        vbox.addWidget(self.push_button)

        self.setLayout(vbox)

    def get_item(self):
        mylist = [
            'علی',
            'محمد',
            'رضا',

        ]
        _item, ok = QInputDialog.getItem(self, 'Title Get Item', 'اسمتو انتخاب کن !', mylist)
        if ok and _item:
            self.line_edit.setText(_item)

    def get_int(self):
        range_data = [20, 50]

        _item, ok = QInputDialog.getInt(self, 'Title Get Int', 'سن خودتون رو انتخاب کنین',*range_data)
        if _item and ok:
            self.line_edit.setText(str(_item))

    def get_text(self):
        _item, ok = QInputDialog.getText(self, 'Title Get Text','پسورد رو وارد کنین')
        if ok and _item:
            self.line_edit.setText(_item)

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())