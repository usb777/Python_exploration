from Home import *

home = Home("Dzmitry", "Samoila",38, "mixed", "developer")  

print (home.first_name)
print (home.last_name)
print ("age = "+str(home.age))
print (vars(home))
home.getProps()
