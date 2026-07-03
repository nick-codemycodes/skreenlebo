from PyQt6.QtCore import QPoint, QRect, Qt
from PyQt6.QtGui import QCursor, QKeyEvent, QPainter, QPen
from PyQt6.QtWidgets import QWidget

from .constants import (
    OVERLAY_COLOR,
    RECTANGLE_BORDER,
    RECTANGLE_COLOR,
)


class Canvas(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setCursor(QCursor(Qt.CursorShape.CrossCursor))

        self.start_point = QPoint()
        self.end_point = QPoint()

        self.selection_rect = QRect()

        self.is_drawing = False

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.fillRect(self.rect(), OVERLAY_COLOR)

        if not self.selection_rect.isNull():
            painter.setPen(
                QPen(
                    RECTANGLE_COLOR,
                    RECTANGLE_BORDER,
                )
            )
            painter.drawRect(self.selection_rect)

    def mousePressEvent(self, event):
        self.start_point = event.position().toPoint()
        self.end_point = self.start_point

        self.selection_rect = QRect(self.start_point, self.end_point)

        self.is_drawing = True

        self.update()

    def mouseMoveEvent(self, event):
        if not self.is_drawing:
            return

        self.end_point = event.position().toPoint()

        self.selection_rect = QRect(
            self.start_point,
            self.end_point,
        ).normalized()

        self.update()

    def mouseReleaseEvent(self, event):
        if not self.is_drawing:
            return

        self.end_point = event.position().toPoint()

        self.selection_rect = QRect(
            self.start_point,
            self.end_point,
        ).normalized()

        self.is_drawing = False

        self.update()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Escape:
            self.close()
            return

        super().keyPressEvent(event)