class A:
    def disp(self):
        print('inside A')

class B:
    def disp(self):
        print('inside B')

class C(A,B):
    def disp(self):
        print('inside c')
c1=C()
c1.disp()
c1.disp()
c1.disp()
