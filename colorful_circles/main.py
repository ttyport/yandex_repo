import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtCore import QSize, Qt, QLine, QPoint
from PyQt5.QtGui import QPainter, QPen, QBrush
from random import randint, choice
from ui import Window


class MainWindow(QMainWindow):
    def __init__(self):
        Window.InitUI(self)

    def draw(self):
        button = self.sender()
        self.line = QLine(QPoint(), button.pos())
        self.update()

    def paintEvent(self, event):
        QMainWindow.paintEvent(self, event)
        if not self.line.isNull():
            painter = QPainter(self)
            colors = [Qt.black, Qt.blue, Qt.white, Qt.red, Qt.green, Qt.yellow, Qt.cyan]
            color = choice(colors)
            pen = QPen(color, 3)
            painter.setPen(pen)
            painter.setBrush(QBrush(color, Qt.SolidPattern))
            x, y = randint(0, 400), randint(0, 400)
            painter.drawEllipse(x, x, y, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
