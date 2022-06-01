from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QThread, pyqtSignal, QRunnable, QThreadPool, QObject
import sys
import time


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PersianPython')
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(200,200, 300, 150)
        vbox = QVBoxLayout()
        btn = QPushButton('Press')
        btn.clicked.connect(self.signal)
        vbox.addWidget(btn)

        self.label = QLabel('')
        self.label.setFont(QFont('arial', 30))
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.pool = QThreadPool()
        # self.worker = WorkerThread()

    def signal(self):
        worker = WorkerThread()
        worker.signals.finished.connect(self.thread_finished)
        self.pool.start(worker)

    def set_text(self, data):
        self.label.setText(data)

    # def func(self):
    #     for i in range(5):
    #         print(i)
    #         # self.label.setText(str(i))
    #         time.sleep(0.5)

    def thread_finished(self):
        print("Thread Tamom Shode Ast !")


class WorkerSignals(QObject):
    finished = pyqtSignal()


class WorkerThread(QRunnable):
    # data_signal = pyqtSignal(str)
    signals = WorkerSignals()

    def run(self):
        for i in range(5):
            print(i)
            # self.label.setText(str(i))
            # self.data_signal.emit(str(i))
            time.sleep(0.5)

        self.signals.finished.emit()


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())