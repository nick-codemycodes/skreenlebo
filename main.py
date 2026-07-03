import sys

from PyQt6.QtWidgets import QApplication, QLabel

def main():
    app = QApplication(sys.argv)
    label = QLabel("Hello, Skreenlebo!")
    label.resize(400, 300)
    label.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()