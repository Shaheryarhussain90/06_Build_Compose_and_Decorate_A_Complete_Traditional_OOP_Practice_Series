
class A:
    def show(self):
        print("show A class")
class B:
    def show(A):
        print("show B class")

class C:
    def show(A):
        print("sow C class")

class D(B, C):
   pass

res = D()
res.show()