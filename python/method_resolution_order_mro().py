class A:
    pass
class B(A):
    pass
class C:
    pass

class D(A,C):
    pass
print(A.mro())
print(B.mro())
print(D.mro())