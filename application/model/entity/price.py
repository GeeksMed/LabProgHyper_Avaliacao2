class Price:
    def __init__(self, value: float, installments: float, installmentValue: float):
        self.__value = value
        self.__installments = installments
        self.__installmentValue = installmentValue

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    @property
    def installments(self):
        return self.__installments

    @installments.setter
    def installments(self, value):
        self.__installments = value

    @property
    def installmentValue(self):
        return self.__installmentValue

    @installmentValue.setter
    def installmentValue(self, value):
        self.__installmentValue = value

    def toDict(self) -> dict:
        return {
            "value": self.__value,
            "installments": self.__installments,
            "installmentValue": self.__installmentValue
        }