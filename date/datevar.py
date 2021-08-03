import datetime

y = datetime.datetime.now()
print(y)


x = datetime.datetime.now()

print("year = ", x.year)
print("month = ", x.month)
print("day = ", x.day)



print(x.strftime("%A"))