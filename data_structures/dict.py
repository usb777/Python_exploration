Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    


def printDict(dictionary):
    for x in dictionary:    
        print(x," : ", dictionary[x]) 
    print("####### end dict #########")
    print("lengh of Dict = ", len(dictionary))

printDict(Employee)



emp1 = Employee.pop('Name')


print(emp1)
print(emp1)
printDict(Employee)