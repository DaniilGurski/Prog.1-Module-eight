import os
import datetime

os.system("cls")

# creating a custom date
custom_date = datetime.date(2023, 8, 16)
print(custom_date)


# getting current date / other info about current date
current_date = datetime.date.today()
print(f"Current date : {current_date}")

print(f"Current day : {current_date.day}")
print(f"Current month : {current_date.month}")
print(f"Current year : {current_date.year}")


# getting the weekday - two ways
# Monday 0 - Sunday 6
current_weekday = current_date.weekday()
# Monday 1 - Sunday 7
current_isoweekday = current_date.isoweekday()


# time delta 
tdelta = datetime.timedelta(days=7) # you can try hours, minutes and so on...
date2 = current_date + tdelta
print(date2)

# if two dates are added, you get time delta
bday = datetime.date(2024, 11, 18)
till_bday = bday - current_date
print(till_bday) # try .days, .total_second

# Time
