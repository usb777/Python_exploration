L1 = ["John", 102, "USA"]    
L2 = [1, 2, 3, 4, 5, 6]   


def printList(listData):
    for lData in listData:
     print (lData) 
    print ("type is ",type(listData)) 
    print (" -----end list-----")

     # end of printTuple fucntion



printList(L1)

printList(L2)
L1.append("Dzmitry")
L1.remove(102)

print ("List1:",L1)
print ("List2:",L2)