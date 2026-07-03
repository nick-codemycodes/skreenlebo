import sys

from PyQt6.QtWidgets import QApplication
from .canvas import Canvas

def start():
    app = QApplication(sys.argv)

    window = Canvas()
    window.showFullScreen()

    sys.exit(app.exec())