import sys

from random import randint
from interface import Interface

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QColor, QPen


class MainWindow(Interface):
    def __init__(self):
        super().__init__()

        self.make_button.clicked.connect(self.make_circle)
        self.clicked = False

    def make_circle(self):
        self.clicked = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.clicked:
            self.draw(qp)
        qp.end()

    def draw(self, qp):
        pen = QPen(Qt.yellow, 4, Qt.SolidLine)
        qp.setPen(pen)
        for _ in range(randint(0, 10)):
            size = randint(10, 100)
            qp.drawArc(randint(0, 800), randint(0, 600), size, size, 0, 360 * 16)

def main():
    app = QApplication(sys.argv)
    program = MainWindow()
    program.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
