class Charger:
    def __init__(self,cname):
        self.cname=cname
        print('charger is ready ')
    def getcharger(self):
        print('charger can be used for charging ')

class Mobile:
    def __init__(self,mname):
        self.mname=mname
        self.c1=''
        print('mobile created')
    def connect(self,c1):
        self.c1=c1
        print('mobile has been connected to charger')

moblie=Mobile('iPhone')
charger=Charger('iPhone Charger')
moblie.connect(charger)
print(moblie.mname)
print(moblie.c1.cname)
moblie.c1.getcharger()
print()
print('after deleting main object')
print(charger.cname)
charger.getcharger()