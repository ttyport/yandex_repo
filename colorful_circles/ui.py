from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtCore import QSize, QLine

class Window:
    def InitUI(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(1000, 500))
        self.setWindowTitle("Colourful Circles")

        button = QPushButton('Draw', self)
        button.clicked.connect(self.draw)
        button.resize(100, 50)
        button.move(450, 400)
        self.line = QLine()
