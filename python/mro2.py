class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(A):
    pass
class E(B):
    pass
class F(B,C):
    pass
class G(C,D):
    pass
class H(D):
    pass
class I(E,F):
    pass
class J(G,H):
    pass
class K(I,J):
    pass


print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
print(E.mro())
print(F.mro())
print(G.mro())
print(H.mro())
print(I.mro())
print(J.mro())
print(K.mro())