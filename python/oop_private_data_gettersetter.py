class Book:
    def __init__(self,value):
        self.__pages=value
    def getdata(self):
        return(self.__pages)
    def setdata(self,value):
        if(value>=1):
            self.__pages=value

b=Book(100)
print(b.getdata())
b.setdata(200)
print(b.getdata())
b.setdata(-99)
print(b.getdata())

