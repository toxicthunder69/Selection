#Joseph Everden
#01/10/14
#Gross Pay

hours = int(input("How many hours did you work this week? "))
pay = float(input("How much are you paid per hour? "))
if hours > 0 and hours <= 60:
    if hours > 40:
        extra_hours = hours - 40
        extra_pay = pay * 1.5
        extra_gross_pay = extra_hours * extra_pay
        hours = 40
    gross_pay = round((hours * pay) + extra_gross_pay, 2)
    print("Your gross pay this week is £{0}".format(gross_pay))
else:
    print("Invalid amount of hours, it needs to be in the range of 0-60.")
    
