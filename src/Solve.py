import galois, Utils
import numpy as np

class Solver:

    def __init__(self, size: int) -> None:
        self.util = Utils.Utils()
        self.size = size 
        self.GF = galois.GF(2)

        self.A = self.util.baseMatrix(self.size)
        self.AInverse, self.null = self.galoisInversion(self.A)

    # we need to see if the null vectors from the base and the config are orthogonal for a solution to exist
    def isSolvable(self, config: np.array) -> bool:
        config = np.asarray(config).ravel()
        return not any([np.dot(x, config) & 1 for x in self.null])

    def gaussJordanElim(self, matrix):
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

    def galoisInversion(self, matrix):
        n = len(matrix)
        matrix = np.hstack([matrix, np.eye(n)])
        B, nulldim = self.gaussJordanElim(matrix)
        
        inverse = np.int_(B[-n:, -n:])
        B = B[:n, :n]
        nullVectors = list()
        if nulldim > 0:
            nullVectors = B[:, -nulldim:]
            nullVectors[-nulldim:, :] = self.GF(np.eye(nulldim))
            nullVectors = np.int_(nullVectors.T)
        return inverse, nullVectors 

    def Solve(self, config: np.array) -> np.array:
        solution = np.dot(self.AInverse, np.asarray(config).ravel()) & 1
        return np.reshape(solution, (self.size, self.size))

