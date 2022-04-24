class demo:
	count=0
	def __init__(self):
		self.x=10
		self.y=20
		demo.count=demo.count+1

d1=demo()
d2=demo()
d3=demo()
print("the no of object in this class : ",demo.count)