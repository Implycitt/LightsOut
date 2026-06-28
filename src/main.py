import torch
from Window import Window
from random import randint
import Solve

if __name__ == "__main__":
    gridDimensions = 5
    #window = Window()
    a = Solve.Solver()
    gridArr: list = [[randint(0, 1) for _ in range(gridDimensions)] for _ in range(gridDimensions)]
    grid: torch.Tensor = torch.tensor(gridArr)
    print(a.Solve(gridArr))

