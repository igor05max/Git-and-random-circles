import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint
from ui import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.draw_)
        self.true = False

    def draw_(self):
        self.true = True
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_cr(qp)
        qp.end()

    def draw_cr(self, qp):
        if self.true:
            self.true = False
            x, y, len_ = randint(20, self.width() - 50), randint(20, self.height() - 50),\
                         randint(20, self.width() // 2)
            qp.setBrush(QColor(randint(10, 255), randint(10, 255), randint(10, 255)))
            qp.drawEllipse(x, y, len_, len_)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
