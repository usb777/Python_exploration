# The control transfer is transfered  
# when break statement soon it sees t  
i = 0  
str1 = 'javatpoint'  

print('############### break #######################') 

while i < len(str1):   
    if str1[i] == 't':   
        i += 1  
        break 
    print('Current Letter :', str1[i])   
    i += 1 

print('############### continue #######################') 

i = 0  
str1 = 'javatpoint'  
while i < len(str1):   
    if str1[i] == 't':   
        i += 1  
        continue 
    print('Current Letter :', str1[i])   
    i += 1 

print('############### classik number loop #######################') 
k=0
while k < 10:   
  
    print('Current number is:',k)   
    k += 1 


print('############### for pass #######################') 
values = {'P', 'y', 't', 'h','o','n'}  
for val in values:  
     pass    
     print('Current number is:',val)  
    