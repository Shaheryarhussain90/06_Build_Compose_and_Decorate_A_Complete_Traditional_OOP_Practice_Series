
class Product:
    def __init__(self, price):
        self.__price = price

    @property

    def price(self):
        return self.__price
    
    @price.setter

    def  price (self, value):
        if value < 0 :
            raise ValueError("price cannot be negative")
        self.__price = value
    @price.deleter

    def price(self):
        print("delete price....")
        del self.__price
    
obj = Product(100)
print(obj.price)

obj.price = 50
print(obj.price)

del obj.price



