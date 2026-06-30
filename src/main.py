import sys

from Window import Window
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
