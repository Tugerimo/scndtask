from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint
import sys

class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)  # ...
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        thickness = randint(1, 200)
        qp.drawEllipse(randint(1, 400), randint(1, 400), thickness, thickness)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec_())
