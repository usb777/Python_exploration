from Home import *

home = Home("Dzmitry", "Samoila",38, "mixed", "developer")  

print (home.first_name)
print (home.last_name)
print ("age = "+str(home.age))
print (vars(home))
home.getProps()

home.setAge(100)
print ("age = "+str(home.age))
print ("age from Get = "+str(home.getAge()))

home.setJob("Developer")
print ("job = "+str(home.job))
print ("job from Get = "+str(home.getJob()))

