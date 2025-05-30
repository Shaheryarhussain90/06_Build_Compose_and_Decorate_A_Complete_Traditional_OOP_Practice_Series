class Employe:
    def __init__(self, name, sallry, ssn):
        self.name = name  #public
        self._sallry = sallry    #proceted
        self.__ssn = ssn    #privte

    def get__ssn(self):
        return self.__ssn
    def __str__(self):
        return f"Name: {self.name}, payment: {self._sallry}, NO: {self.__ssn}"

employe2 = Employe("shaheryar", 10000, "03172662591")
print(employe2)