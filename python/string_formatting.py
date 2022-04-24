# string formatting

name=input("enter name : ")


# other program
age=input("enter age :")
marks=input("enter marks :")

print("Hello {}".format(name))
#way 1
print("Name ={} \n Age = {} \n Marks ={}".format(name,age,marks))
#             0           1         2    #        0   1     2
#index of name ->0,age->1,marks->2

#way 2
print("Name ={2} \n Age = {0} \n Marks ={1}".format(age,marks,name))
#             2            0             1         0     1    2
#way3
print("name ={}".format(name))
print("name ={}".format(age))
print("name ={}".format(marks))
#way 3
