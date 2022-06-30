from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, \
    QGraphicsItem, QGraphicsRectItem
from PyQt6.QtGui import QIcon, QKeyEvent
from PyQt6.QtCore import Qt
import sys


class MyRect(QGraphicsRectItem):
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Left:
            self.setPos(self.x() - 10, self.y())
        elif event.key() == Qt.Key.Key_Right:
            self.setPos(self.x() + 10, self.y())

        elif event.key() == Qt.Key.Key_Up:
            self.setPos(self.x(), self.y() - 10)

        elif event.key() == Qt.Key.Key_Down:
            self.setPos(self.x(), self.y() + 10)


class Window(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))
        # self.setGeometry(200, 200, 700, 400)
        self.setFixedSize(800, 600)
        scene = QGraphicsScene()
        # rect = QGraphicsRectItem(0, 0, 200, 200)
        rect = MyRect(0, 0, 200, 200)
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        rect.setFocus()
        scene.addItem(rect)
        self.setScene(scene)




app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
