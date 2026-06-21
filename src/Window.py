import torch, sys

from random import randint
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

gridDimensions: int = 5
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
            for j, element in enumerate(row):
                buttonArr.append(Button(element, int(gridDimensions*i + j)))
                self.gridLayout.addWidget(buttonArr[-1], j, i)

        self.window.show()
        sys.exit(self.app.exec())


class Button(QPushButton):

    state: int = 0
    index: int = 0
    green: str = "background-color: green; border: 2px solid white"
    red: str = "background-color: red; border: 2px solid white"

    def __init__(self, state: int, index: int):
        super().__init__()
        self.setMinimumSize(100, 100)
        self.setMaximumSize(300, 300)
        self.state = state
        self.index = index
        self.updateStyle()

        self.clicked.connect(self.press)

    def press(self) -> None:
        neighbors: dict = {
                "up": self.index - gridDimensions,
                "down": self.index + gridDimensions,
                "left": self.index - 1,
                "right": self.index + 1,
                "noop": self.index
        }

        for direction in neighbors:
            if neighbors[direction] < 0 or neighbors[direction] >= gridDimensions**2:
                continue
            buttonArr[neighbors[direction]].completeUpdate()

    def updateStyle(self) -> None:
        self.setStyleSheet(self.green) if (self.state) else self.setStyleSheet(self.red)

    def updateState(self) -> None:
        self.state += 1
        self.state %= 2

    def completeUpdate(self) -> None:
        self.updateState()
        self.updateStyle()
