Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])    
print(Days)    
print(type(Days))    
print("looping through the set elements ... ")    
for i in Days:    
    print(i)   


print("#####################")
setData = {"John", 1, "Lost", 3,4,5}

for k in setData:    
    print(k) 

print (" ---------")
def printSet(setData):
    for sData in setData:
     print (sData) 
    print (" -----end Set-----")
     # end of printTuple fucntion


Days.update(["Never day", "Empty Day"])

printSet(Days)

Days.discard("Never day") # No error if element doesnt exist
Days.discard("Never day")
Days.remove("Never day")
print(Days)


