import sys

from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QApplication


class Window(QObject):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
engine = QQmlApplicationEngine()

window = Window()

engine.rootContext().setContextProperty('window', window)

engine.load('window.qml')

sys.exit(app.exec())
