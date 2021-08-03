import datetime
from datetime import timedelta

y = datetime.datetime.now()
print(y)


x = datetime.datetime.now()
z = x -  timedelta(days = 1)  # previous day

print("year = ", x.year)
print("month = ", x.month)
print("day = ", x.day)
print("type year = ", type(x.year))



day =""

if   len(str(x.month)) == 1: monthNumber = '0'+str(x.month)
else: monthNumber = str(x.month)
print("month Number = ", monthNumber)

if   len(str(x.day)) == 1: dayNumber = '0'+str(x.day)
else: dayNumber = str(x.day)
print("day Number = ", dayNumber)

# Checking of Data
dayZ  = 22
if   len(str(dayZ)) == 1: dayNumberZ = '0'+str(dayZ)
else: dayNumberZ = str(dayZ)
print("day Big Number = ", dayNumberZ)


dateString = str(x.year)+monthNumber+dayNumber
print("YYYYmmdd = "+dateString)

fileName = "zztop20210803.avro"

if dateString in fileName: print("contain data")
else : print("don't contain")



def _createCurrentDateStringYYYYmmdd(x = datetime.datetime.now()):
    if   len(str(x.month)) == 1: monthNumber = '0'+str(x.month)
    else: monthNumber = str(x.month)
    #print("month Number = ", monthNumber)

    if   len(str(x.day)) == 1: dayNumber = '0'+str(x.day)
    else: dayNumber = str(x.day)
    #print("day Number = ", dayNumber)
    return str(x.year)+monthNumber+dayNumber
      




print(" prevous day year = ", z.year)
print(" prevous day month = ", z.month)
print(" prevous day = ", z.day)


fileName = "zztop20210802"

print(x.strftime("%A"))

print(str(1)+'f')

print("lengt = ", len("Abba"))

x = datetime.datetime.now()

print(" YYYYmmdd = ",_createCurrentDateStringYYYYmmdd(x))

z = x -  timedelta(days = 1)  # previous day
print("previous day YYYYmmdd = ",_createCurrentDateStringYYYYmmdd(z))