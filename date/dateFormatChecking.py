import datetime

dt  = datetime.datetime.now() 


print (dt.strftime ("%d / %m / %Y ")) # represents the date in DD/ MM/ YYYY  

print (dt.strftime ("%Y-%m-%d")) # represents the date in DD/ MM/ YYYY 
print (dt.strftime (" %I: %M: %S %p ")) # represents the time in HH: MM: SS AM/ PM  
print (dt.strftime ("%a, %b %d, %Y ")) # represents the day, month date and year 




strDate = dt.strftime ("%Y-%m-%d")

print ("Today date is",strDate )

print ("hello world")




#https://medium.com/@ajeet214/conversion-between-datetime-object-and-string-in-python-b1bc527a18