from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(200,200, 700, 300)

        vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.selectionChanged.connect(self.signal)
        self.calendar.setGridVisible(True)
        vbox.addWidget(self.calendar)
        self.label = QLabel('')
        self.label.setFont(QFont('arial', 26))
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def signal(self):
        print(self.calendar.selectedDate().toString('yyyy/M/d'))
        self.label.setText(str(self.calendar.selectedDate().toPyDate()))
        # datetime.date

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())