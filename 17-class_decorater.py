
def add_greeting(cls):
    def greet(self):
        return "Helo from decorater"
    cls.greet = greet
    return cls

@add_greeting

class Person:
    def __init__(self, name):
        self.name = name


res = Person("Shaheryar")
print(res.greet())