
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.bread = breed
    
    def speak(self):
        print( f"{self.name},  is says wool")

dog1 = Dog("Tommy", "Greman ")
dog1.speak()