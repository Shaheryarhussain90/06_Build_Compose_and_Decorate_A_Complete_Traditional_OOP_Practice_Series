
class InvalidAgeError(Exception):
     def __init__(self, age, message):
        self.age = age
        self.message = message
        super().__init__(f"{self.message}, provded age {self.age}")
    
def check_age(age):
    if age > 18:
        raise InvalidAgeError(age)
    else:
            print("age is provide")
try:
    user_age = int(input("Enter Your age"))
    check_age(user_age)

except InvalidAgeError as e:
    print("Invalidageerror is Caugth", e)

except ValueError:
     print("please enter a valid enter is age23")


