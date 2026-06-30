import sys, time

from random import randint
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
import numpy.typing as npt

from Solve import Solver

gridDimensions: int = 5 
buttonArr: list = list()

class Window(QApplication):

    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.gridLayout = QGridLayout()
        self.Solver = Solver(gridDimensions)
        self.gridArr: list = list()

        self.window.setLayout(self.gridLayout)
        self.window.setGeometry(100, 100, 1000, 800)

        self.mainLoop()
        self.solve()

        self.window.show()
        sys.exit(self.app.exec())

    def mainLoop(self) -> None:
        while not self.Solver.isSolvable(self.gridArr):
            self.gridArr = [[randint(0, 1) for _ in range(gridDimensions)] for _ in range(gridDimensions)]

        for i, row in enumerate(self.gridArr):
            rowArr: list = list()
            for j, element in enumerate(row):
                rowArr.append(Button(element, [i, j]))
                self.gridLayout.addWidget(rowArr[-1], i, j)
            buttonArr.append(rowArr)

    def clearScreen(self) -> None:
        for i in reversed(range(self.gridLayout.count())): 
            try:
                self.gridLayout.itemAt(i).widget().setParent(None)
            except:
                continue

    def solve(self) -> None:
        solution: npt.NDArray = self.Solver.Solve(self.gridArr)
        print(solution)

class Button(QPushButton):

    def __init__(self, state: int, index: list):
        super().__init__()

        self.green: str = "background-color: green; border: 2px solid white"
        self.red: str = "background-color: red; border: 2px solid white"

        self.setMinimumSize(100, 100)
        self.setMaximumSize(300, 300)
        self.state: int = state
        self.index: list = index
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
