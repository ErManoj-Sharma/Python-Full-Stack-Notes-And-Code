from faker import Faker
f=Faker()
name=f.name()
print("Genrated fake name=" , name)
address=f.address ()
print("Generated fake address=",address)
text=f.text()
print("Generated fake text=",text)
date=f.date()
print("Generated fake date=",date)
dob=f.date_pf_birth()
print("Generated fake DOB=",dob)

random=f.random_int(min=10,max=100)
print("Generated fake number=",random)

email=f.email()
print("Generated fake email=",email)