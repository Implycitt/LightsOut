import torch, sys

from random import randint
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

from Solve import Solver

gridDimensions: int = 3 
buttonArr: list = list()

class Window(QApplication):

    app = QApplication(sys.argv)
    window = QWidget()
    gridLayout = QGridLayout()

    def __init__(self) -> None:
        gridArr: list = [[randint(0, 1) for _ in range(gridDimensions)] for _ in range(gridDimensions)]
        grid: torch.Tensor = torch.tensor(gridArr)

        self.window.setLayout(self.gridLayout)
        self.window.setGeometry(100, 100, 1000, 800)

        for i, row in enumerate(gridArr):
            rowArr: list = list()
            for j, element in enumerate(row):
                rowArr.append(Button(element, [i, j]))
                self.gridLayout.addWidget(rowArr[-1], i, j)
            buttonArr.append(rowArr)

        Solver.gaussJordanElim(grid, gridArr)

        self.window.show()
        sys.exit(self.app.exec())


class Button(QPushButton):

    state: int = 0
    index: list = list()
    green: str = "background-color: green; border: 2px solid white"
    red: str = "background-color: red; border: 2px solid white"

    def __init__(self, state: int, index: list):
        super().__init__()
        self.setMinimumSize(100, 100)
        self.setMaximumSize(300, 300)
        self.state = state
        self.index = index
        self.updateStyle()

        self.clicked.connect(self.press)

    def press(self) -> None:
        neighbors: dict = {
                "up": [self.index[0] + 1, self.index[1]],
                "down": [self.index[0] - 1, self.index[1]],
                "left": [self.index[0], self.index[1] - 1],
                "right": [self.index[0], self.index[1] + 1],
                "noop": self.index
        }

        for direction in neighbors:
            i, j = neighbors[direction]
            try:
                if (i == -1 or j == -1):
                    continue
                buttonArr[i][j].completeUpdate()
            except IndexError:
                continue

    def updateStyle(self) -> None:
        self.setStyleSheet(self.green) if (self.state) else self.setStyleSheet(self.red)

    def updateState(self) -> None:
        self.state += 1
        self.state %= 2

    def completeUpdate(self) -> None:
        self.updateState()
        self.updateStyle()
