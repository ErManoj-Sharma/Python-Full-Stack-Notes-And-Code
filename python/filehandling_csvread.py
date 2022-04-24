import csv
fptr=open("emp.csv",'r')
r=csv.reader(fptr)
print(r)
data=list(r)
print(data)
print()
for rec in data:
    print(rec)

print()
for rec in data:
    for field in rec:
        print(field,end=' ')
    print()

fptr.close()
