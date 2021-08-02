T1 = (101, "Peter", 22)    
T2 = ("Apple", "Banana", "Orange")     
T3 = 10,20,30,40,50  
  
print(type(T1))  
print(type(T2))  
print(type(T3)) 

for t in T1:
    print (t) 

def printTuple(tupleData):
    for tData in tupleData:
     print (tData) 
    print (" -----end-----")
     # end of printTuple fucntion

printTuple(T1)
printTuple(T2)
printTuple(T3)


print ("T[1] = ", T1[1])