from abc import abstractmethod, ABC

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, Width, Heigt):
        self.width = Width
        self.height = Heigt
    
    def area(self):
        return self.width * self.height
rect = Rectangle(4, 5)
print(rect.area())