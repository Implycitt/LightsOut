import torch, sys

from random import randint
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class Window(QApplication):

    gridDimensions: int = 3

    def __init__(self) -> None:
        app = QApplication(sys.argv)
        window = QWidget()
        grid = QGridLayout()

        window.setLayout(grid)
        window.setGeometry(800, 600, 200, 100)
        window.show()
        sys.exit(app.exec())

    # create grid
    def setup(self) -> None:
        gridArr: list = [[randint(0, 1) for i in range(self.gridDimensions)] for i in range(self.gridDimensions)]
        grid: torch.Tensor = torch.tensor(gridArr)


    # button update

    
