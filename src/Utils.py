class Utils:
    def convertButtonArray(self, buttonArray: list) -> list:
        convertedArray: list = list()

        for button in buttonArray:
            convertedArray.append(button.state)

        return convertedArray
    

