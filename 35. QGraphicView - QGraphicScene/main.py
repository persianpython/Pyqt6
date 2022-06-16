from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt6.QtGui import QIcon, QFont, QPen, QBrush
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(200, 200, 700, 400)
        scene = QGraphicsScene()
        redpen = QPen(Qt.GlobalColor.red, 7)

        yellow_brush = QBrush(Qt.GlobalColor.yellow)
        blue_brush = QBrush(Qt.GlobalColor.blue)

        ellipse = scene.addEllipse(100, 100, 200, 200, redpen, yellow_brush)
        rect = scene.addRect(-100, -100, 200, 200, redpen, blue_brush)

        ellipse.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

        view = QGraphicsView(scene, self)
        view.setGeometry(0,0 ,650, 400)



app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
