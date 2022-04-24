class A:
    def dispa(self):
        print('inside A')

class B:
    def dispb(self):
        print('inside B')

class C(A,B):
    def dispc(self):
        print('inside c')
c1=C()
c1.dispa()
c1.dispb()
c1.dispc()
