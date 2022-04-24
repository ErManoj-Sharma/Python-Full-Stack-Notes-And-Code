class A:
    def display(self):
        print('inside A')
class B(A):
    def display(self):
        print('inside B ')
class C(B):
    def display(self):
        print('inside c')
class D(C):
    def dispD(self):
        A.display(self)
        B.display(self)
        C.display(self)
d=D()
d.dispD()