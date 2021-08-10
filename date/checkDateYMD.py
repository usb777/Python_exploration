import datetime

def isValidDateFormat(dateString):
    date_string=dateString
    date_format="%Y-%m-%d"

    try:
        date_obj=datetime.datetime.strptime(date_string, date_format)
    except ValueError:
        print("Incorrect data format, should be YYYY-mm-dd")
    else: 
        print("good format")

isValidDateFormat("2021-08-08")

isValidDateFormat("20210808")