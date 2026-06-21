import torch, sys

from random import randint
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class Window(QApplication):

    gridDimensions: int = 5
    app = QApplication(sys.argv)
    window = QWidget()
    gridLayout = QGridLayout()

    def __init__(self) -> None:
        gridArr: list = [[randint(0, 1) for _ in range(self.gridDimensions)] for _ in range(self.gridDimensions)]
        buttonArr: list = list()
        grid: torch.Tensor = torch.tensor(gridArr)

        self.window.setLayout(self.gridLayout)
        self.window.setGeometry(100, 100, 1000, 800)

        for i, row in enumerate(gridArr):
            for j, element in enumerate(row):
                buttonArr.append(Button(element))
                self.gridLayout.addWidget(buttonArr[-1], i, j)

        self.window.show()
        sys.exit(self.app.exec())

    def press(self, buttonIndex: int) -> None:
        up: int = buttonIndex - self.gridDimensions
        down: int = buttonIndex + self.gridDimensions
        left: int = buttonIndex - 1
        right: int = buttonIndex + 1

class Button(QPushButton):
    state = 0

    def __init__(self, state: int):
        super().__init__()
        self.state = state
        self.setup()

    def setup(self):
        green: str = "background-color: green; border: 2px solid white"
        red: str = "background-color: red; border: 2px solid white"

        self.setStyleSheet(green) if (self.state) else self.setStyleSheet(red)

        self.setMinimumSize(100, 100)
        self.setMaximumSize(300, 300)
