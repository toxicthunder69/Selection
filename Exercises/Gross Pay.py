#Joseph Everden
#25/09/14
#Gross pay calculator

work_hours = int(input("Enter the amount of hours you work between 0 and 60: "))
work_rate = float(input("Enter the rate in which you are paid in £'s: "))
if work_hours > 40 and work_hours <= 60:
    extra_hours = 60 - work_hours
    work_hours = 40
    gross_pay = (work_hours * work_rate) + (extra_hours * work_rate)
    print("")

