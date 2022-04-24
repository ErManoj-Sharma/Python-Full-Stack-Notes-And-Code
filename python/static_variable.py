class demo:
    x=777
    y=666
    def __init__(self):
        self.a=11
        self.b=22

d1=demo()
d2=demo()
d3=demo()

print(d1.a)
print(d1.b)
print(d2.a)
print(d2.b)
print(d3.a)
print(d3.b)

print(demo.x)
print(demo.y)

# changing value of static varible
demo.x=888
demo.y=999
print(demo.x)
print(demo.y)

#if we try
d1.x=102
print(d1.x)
print(demo.x)