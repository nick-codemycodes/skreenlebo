from PyQt6.QtCore import QPoint, QRect, Qt
from PyQt6.QtGui import QColor, QPainter, QPen
from PyQt6.QtWidgets import QWidget


class Canvas(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.start = QPoint()
        self.end = QPoint()
        self.drawing = False

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.fillRect(self.rect(), QColor(0, 0, 0, 30))

        if self.drawing:
            painter.setPen(QPen(QColor("cyan"), 2))
            painter.drawRect(QRect(self.start, self.end).normalized())

    def mousePressEvent(self, event):
        self.start = event.position().toPoint()
        self.end = self.start
        self.drawing = True
        self.update()

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.end = event.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, event):
        self.end = event.position().toPoint()
        self.update()