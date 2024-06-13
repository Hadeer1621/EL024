# Print the calendar of a given month and year

import calendar
# enter the input year and month

year = int(input("please enter the year : "))
month = int(input("please enter the Month : "))

# check month 
if month < 1 or month > 12:
    print("Invaild month . please enter a number between 1 to 12 ")
else:
    Calendar_var = calendar.month(year,month)

# Print the calendar for the specified year and month
print("Calendar for {}-{}".format(year, month)) 
# we will display the calendar 
print(Calendar_var) 

