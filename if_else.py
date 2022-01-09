a  =3
if a>4 :  print ('a is bigger then 4')
else : print('a is smaller')




b = -5
 
if b == 0 :
    print('b is zero.')
elif b > 0:
    print('b is positive.')
elif b < 0:
    print('b is negative.')


def chooser(a=5):
  if a==5:  print (str(a)+" equal 5")
  elif (a>5): print (str(a)+" more then 5")
  elif (a<5): print (str(a)+" less then 5")

def chooser_return(a=5):
  if a==5:
          print (str(a)+" equal 5")
          
  elif (a>5):
          print (str(a)+" more then 5")
          a=a+1
  elif (a<5):
          print (str(a)+" less then 5")
          a=a-1
  return a
  
  
chooser(10)
print("a stay "+str(chooser_return(100)))
