import sys

from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QObject, pyqtSlot
from PyQt6.QtWidgets import QApplication


class Window(QObject):
    def __init__(self):
        super().__init__()

    @pyqtSlot(bool)
    def hello(self, data):
        print(data)
        print("Hellow !")


app = QApplication(sys.argv)
engine = QQmlApplicationEngine()

window = Window()

engine.rootContext().setContextProperty('window', window)

engine.load('window.qml')

sys.exit(app.exec())
