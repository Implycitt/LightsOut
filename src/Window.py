import sys

from random import randint
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import QTimer
import numpy.typing as npt

from Solve import Solver

gridDimensions: int = 5 
buttonArr: list = list()
gridArr: list = []

class Window(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.mainLayout = QVBoxLayout()

        self.topLayout = QHBoxLayout()
        
        self.newButton = QPushButton("New")
        self.solveButton = QPushButton("Solve")
        
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.newButton)
        self.newButton.clicked.connect(self.clearScreen)
        self.topLayout.addWidget(self.solveButton)
        self.solveButton.clicked.connect(self.solve)

        self.topLayout.addStretch()

        self.gridLayout = QGridLayout()
        self.Solver = Solver(gridDimensions)

        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.gridLayout)

        self.setLayout(self.mainLayout)
        self.setGeometry(100, 100, 1000, 800)

        self.mainLoop()

    def mainLoop(self) -> None:
        global gridArr
        while not self.Solver.isSolvable(gridArr):
            gridArr = [[randint(0, 1) for _ in range(gridDimensions)] for _ in range(gridDimensions)]

        for i, row in enumerate(gridArr):
            rowArr: list = list()
            for j, element in enumerate(row):
                rowArr.append(Button(element, [i, j]))
                self.gridLayout.addWidget(rowArr[-1], i, j)
            buttonArr.append(rowArr)

    def clearScreen(self) -> None:
        global gridArr
        for i in reversed(range(self.gridLayout.count())): 
            try:
                self.gridLayout.itemAt(i).widget().setParent(None)
            except:
                continue
        
        gridArr = list()
        buttonArr.clear()
        self.mainLoop()

    def solve(self) -> None:
        global gridArr
        solution: npt.NDArray = self.Solver.Solve(gridArr)
        self.press: list = list()
        for i in range(len(solution)):
            for j in range(len(solution[i])):
                if solution[i][j]:
                    self.press.append(buttonArr[i][j])
        self.seqPress()

    def seqPress(self) -> None:
        if self.press == []:
            return

        self.press.pop().press()
        QTimer.singleShot(1000, self.seqPress)

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
        global gridArr
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
                gridArr[i][j] = (gridArr[i][j] + 1) % 2
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
