
a = 10

print ("a = ", a,";")

try:
      x = 10
      print(x)
      x/0
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")  
