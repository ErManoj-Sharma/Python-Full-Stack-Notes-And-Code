class A:
    def disp(self):
        print('inside A')

class B:
    def disp(self):
        print('inside B')

class C(B,A): # if (B,A) or (A,B)
    def dispC(self):
        print('inside c')
c1=C()
c1.dispC()
c1.disp()

