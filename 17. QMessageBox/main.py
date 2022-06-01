from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtGui import QIcon, QFont


import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(200,200, 700, 300)
        pushbtn = QPushButton('test')
        pushbtn.clicked.connect(self.show_popup)
        vbox = QVBoxLayout()
        vbox.addWidget(pushbtn)
        self.setLayout(vbox)

    def show_popup(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle('Show MessageBox Title')
        msgbox.setText('Show MessageBox Text')
        msgbox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msgbox.buttonClicked.connect(self.signal_msgbox)
        # msgbox.setDetailedText('Detaile Text')
        msgbox.setIcon(QMessageBox.Icon.Warning)
        msgbox.setInformativeText('Information Text')
        msgbox.exec()

    def signal_msgbox(self, btn):
        print(btn.text())

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())