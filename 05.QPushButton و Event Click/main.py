from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMenu
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

        self.label = QLabel(self)
        # self.label.setFont(QFont('Arial', 20, QFont.Weight.Black))
        # image = QPixmap('logo2.png')
        # self.label.setPixmap(image)
        self.label.move(40, 60)
        self.movie = QMovie('cat.gif')
        # self.movie.setSpeed(500)
        self.label.setMovie(self.movie)
        self.movie.start()

        self.button = QPushButton('QPushButton', self)
        self.button.setGeometry(200, 0, 100, 50)
        self.button.setFont(QFont('Arial', 7, QFont.Weight.ExtraBold))
        self.button.setIcon(QIcon('logo.png'))
        self.button.setIconSize(QSize(50, 50))

        menu = QMenu()
        menu.addAction('Copy')
        menu.addAction('Past')
        menu.addAction('Cut')
        menu.setFont(QFont('Arial', 5, QFont.Weight.ExtraBold))
        menu.setStyleSheet('background-color:red')
        # self.button.setMenu(menu)

        self.button.clicked.connect(self.clicked)

    def clicked(self):
        self.movie.stop()


window = MyWindow()

window.show()

sys.exit(app.exec())
