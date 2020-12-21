import sys
from PyQt5.QtWidgets import QMainWindow,QPushButton, QApplication
from PyQt5.QtCore import QSize, Qt, QLine, QPoint
from PyQt5.QtGui import QPainter, QPen, QBrush
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(1000, 500))
        self.setWindowTitle("Yellow Circle")

        button = QPushButton('Draw', self)
        button.clicked.connect(self.draw)
        button.resize(100, 50)
        button.move(450, 400)
        self.line = QLine()

    def draw(self):
        button = self.sender()
        self.line = QLine(QPoint(), button.pos())
        self.update()

    def paintEvent(self,event):
        QMainWindow.paintEvent(self, event)
        if not self.line.isNull():
            painter = QPainter(self)
            pen = QPen(Qt.yellow, 3)
            painter.setPen(pen)
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            x, y = randint(0, 400), randint(0, 400)
            painter.drawEllipse(x, x, y, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
