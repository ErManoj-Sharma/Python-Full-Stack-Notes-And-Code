class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(A):
    pass
class E(B,C):
    pass
class F(C,D):
    pass
class G(E,F):
    pass

print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
print(E.mro())
print(F.mro())
print(G.mro())