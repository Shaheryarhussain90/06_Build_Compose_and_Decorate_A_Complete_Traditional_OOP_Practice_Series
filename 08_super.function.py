
class Person:
    def __init__(self, name, rolllno):
        self.name = name
        self.rollno = rolllno
class Teacher(Person):
    def __init__(self, name ,rollno, subject ):
        super().__init__( name, rollno)
        self.subject = subject

        
        
s1 = Teacher("shaheryar", 188915 , "Agentic AI")
print(s1.name, s1.rollno, s1.subject)   
