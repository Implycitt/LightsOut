import galois, Utils
import numpy as np
import numpy.typing as npt

from operator import add
from itertools import chain, combinations
from functools import reduce

class Solver:

    def __init__(self, size: int) -> None:
        self.util = Utils.Utils()
        self.size = size 
        self.GF = galois.GF(2)

        self.A = self.util.baseMatrix(self.size)
        self.AInverse, self.null = self.galoisInversion(self.A)

    # we need to see if the null vectors from the base and the config are orthogonal for a solution to exist
    def isSolvable(self, config: list) -> bool:
        assert config.shape[0] == config.shape[1] == self.size, "incompatible shape"
        config = self.GF(np.int_(np.asarray(config).ravel()))
        return not any([np.dot(x, config) & 1 for x in self.null])

    def gaussJordanElim(self, matrix: npt.NDArray) -> tuple[npt.NDArray, int]:
        nulldim = 0
        for i, row in enumerate(matrix):
            pivot = matrix[i:, i].argmax() + i
            if matrix[pivot, i] == 0:
                nulldim = len(matrix) - i
                break
            newRow = matrix[pivot] / matrix[pivot, i]
            matrix[pivot] = matrix[i]
            row[:] = newRow
            
            for j, row2 in enumerate(matrix):
                if j != i:
                    row2[:] -= newRow * matrix[j, i]
        return matrix, nulldim

    def galoisInversion(self, matrix: npt.NDArray) -> tuple[npt.NDArray, list]:
        n = len(matrix)
        matrix = np.hstack([matrix, np.eye(n)])
        B, nulldim = self.gaussJordanElim(self.GF(np.int_(matrix)))
        
        inverse = np.int_(B[-n:, -n:])
        B = B[:n, :n]
        nullVectors = list()
        if nulldim > 0:
            nullVectors = B[:, -nulldim:]
            nullVectors[-nulldim:, :] = self.GF(np.int_(np.eye(nulldim)))
            nullVectors = np.int_(nullVectors.T)
        return inverse, nullVectors 

    def powerset(self, iterable) -> list:
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

    def Solve(self, config: npt.NDArray) -> npt.NDArray:
        if not self.isSolvable(config):
            raise ValueError("Unsolvable")

        solution = np.dot(self.GF(self.AInverse), self.GF(np.asarray(config).ravel())) & 1
        power: list = list(self.powerset(self.null.view(np.ndarray)))
        solutions = []
        for x in power:
            a = reduce(add, x, 0) & 1
            b = solution + self.GF(a)
            solutions.append(np.asarray(b.tolist()))
        final = min(solutions, key=lambda x: x.sum())
        return np.reshape(final, (self.size, self.size))
