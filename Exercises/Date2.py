#Joseph Everden
#02/10/14
#Date Program 2

day_input = int(input("Enter the day (dd): "))
month_input = int(input("Enter the month (m): "))
year_input = int(input("Enter the year (yy): "))
month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
month_input = month_input - 1
month_display = month[month_input]

if day_input == 1:
    day_input = str(day_input + "st")
elif day_input == 2:
    day_input = str(day_input + "nd")
elif day_input == 3:
    day_input = str(day_input + "rd")
else:
    day_input = str(day_input + "th")


