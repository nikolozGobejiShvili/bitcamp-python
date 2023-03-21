import datetime


months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date= input("Date: ")

    try:
        date1 = datetime.datetime.strptime(date, "%d/%m/%Y" , )
    except ValueError:
        print("try again")    
        continue


    print(date1.strftime('%Y/%m/%d'))