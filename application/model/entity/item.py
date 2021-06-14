from application.model.entity.price import Price

class Produto:
    def __init__(self, id: int, name: str, images: list, price: Price):
        self.__id = id
        self.__name = name
        self.__images = images
        self.__price = Price(price['value'], price['installments'], price['installmentValue'])

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def images(self):
        return self.__images

    @images.setter
    def images(self, value):
        self.__images = value

    def add_images(self, value):
        self.__images.append(value)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def toDict(self) -> dict:
        return {
            "id": self.__id,
            "name": self.__name,
            "images": self.__images,
            "price": self.__price
        }

