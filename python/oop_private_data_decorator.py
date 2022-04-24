class Person:
    def __init__(self):
        self.__name=''
    @property
    def dataAccess(self):
        return self.__name
    @dataAccess.setter
    def dataAccess(self,value):
        self.__name=value

p1=Person()
p1.dataaccess='Manoj'
result=p1.dataaccess
print(result)