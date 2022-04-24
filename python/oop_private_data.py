#case 1
print('case 1:')
class Mbook:
    def __init__(self,value):
        self.pages=value


b=Mbook(100)
print(b.pages)
b.pages=200
print(b.pages)
b.pages=-99
print(b.pages)
print()
print('case 2 :')
#case 2
class Book:
    def __init__(self,value):
        self.__page=value

b1=Book(100)
#print(b1.__page) we got error because we cant access private data outside class
b1.__page=300
print(b1.__page)    # it gives output because it id different copy , it is not private data copy .
print()
print('case 3:')

class Abook:
    def __init__(self,value):
        self.__pages=value
    def display(self):
        print(self.__pages)

b2=Abook(100)
#print(b2.__pages)
b2.__pages=-99
print(b2.__pages)
b2.display()