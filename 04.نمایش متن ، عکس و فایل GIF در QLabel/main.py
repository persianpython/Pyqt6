from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie

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
        # self.label.setFont(QFont('Arial', 20))
        # image = QPixmap('logo2.png')
        # self.label.setPixmap(image)
        self.label.move(40, 60)
        movie = QMovie('cat.gif')
        # movie.setSpeed(500)
        self.label.setMovie(movie)
        movie.start()

        # movie.stop()




window = MyWindow()

window.show()

sys.exit(app.exec())
