class Person:
    def __init__(self):
        self.__name=''
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name=value
    getset=property(getter,setter)

p1=Person()
p1.getset='RAMU'
result=p1.getset
print(p1.getset)
print(result)