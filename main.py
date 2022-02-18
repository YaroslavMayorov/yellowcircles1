import sys
from random import randint

from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class Calc(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.button.clicked.connect(self.paint)
        self.flag = False
        self.circles = []

    def paintEvent(self, event):
        QWidget.paintEvent(self, event)
        if self.flag:
            painter = QPainter(self)
            pen = QPen()  # creates a default pen
            pen.setStyle(Qt.SolidLine)
            pen.setWidth(3)
            pen.setBrush(Qt.yellow)
            painter.setPen(pen)
            x = randint(0, 610)
            y = randint(0, 390)
            w = randint(30, 600)
            while x + w > 640 or y + w > 420:
                x = randint(0, 610)
                y = randint(0, 390)
                w = randint(30, 600)
            self.circles.append(x)
            self.circles.append(y)
            self.circles.append(w)
            for i in range(0, len(self.circles), 3):
                tmp = self.circles[i + 2]
                painter.drawEllipse(self.circles[i], self.circles[i + 1], tmp, tmp)
            self.flag = False

    def paint(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calc()
    ex.show()
    sys.exit(app.exec())
