class Os:
    def __init__(self):
        self.status=True
        print('os is installing ')
    def getos(self):
        print('os is executing ')
class Mobile:
    def __init__(self):
        self.mname="MJ"
        self.o=Os()
        print('mobile is created')
        print('Os installed ')
m=Mobile()
print(m.mname)
print(m.o.status)
m.o.getos()

# deleteing main object
del m
print(m.o.status)
m.o.getos()