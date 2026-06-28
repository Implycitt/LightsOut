import numpy as np
from scipy import ndimage

class Utils:
    def convertButtonArray(self, buttonArray: list) -> list:
        convertedArray: list = list()

        for button in buttonArray:
            convertedArray.append(button.state)

        return convertedArray

    def baseMatrix(self, size: int):
        a = np.eye(size*size)
        a = np.reshape(a, (size*size, size, size))
        a = np.asarray(list(map(ndimage.binary_dilation, a)))
        return np.reshape(a, (size*size, size*size))
    

