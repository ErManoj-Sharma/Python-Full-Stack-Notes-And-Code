student={
            "name":'Manoj',
            "age":22,
            "phnum":
                    {
                        "tel":777,
                        "mob":999
                    },
            "test":{
                        "t1":23,
                        "t2":71,
                        "t3":83
                }
        }
print(student)
s1=student.copy()
print(student['phnum']['tel'])
print(s1['phnum']['tel'])
student['phnum']['tel']=888
print(student['phnum']['tel'])
print(s1['phnum']['tel'])
print()
# deepcopy
import copy
s2=copy.deepcopy(student)
print(student['phnum']['tel'])
print(s2['phnum']['tel'])
student['phnum']['tel']=333
print(student['phnum']['tel'])
print(s2['phnum']['tel'])

