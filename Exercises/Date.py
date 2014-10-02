#Joseph Everden
#02/10/14
#Date Program

day = int(input("Enter the day (dd): "))
month = int(input("Enter the month (m): "))
year = int(input("Enter the year (yy): "))

if month <= 0 or month > 12:
    print("You entered an invalid number for the month!")
if month == 1:
    month = "January"
if month == 2:
    month = "February"
if month == 3:
    month = "March"
if month == 4:
    month = "April"
if month == 5:
    month = "May"
if month == 6:
    month = "June"
if month == 7:
    month = "July"
if month == 8:
    month = "August"
if month == 9:
    month = "September"
if month == 10:
    month = "October"
if month == 11:
    month = "November"
if month == 12:
    month = "December"
if day == 1:
    print("The date you entered is: 1st {0} {1}.".format(month,year))
elif day == 2:
    print("The date you entered is: 2nd {0} {1}.".format(month,year))
if day == 3:
    print("The date you entered is: 3rd {0} {1}.".format(month,year))
else:
    print("The date you entered is: {0}th {1} {2}.".format(day,month,year))
