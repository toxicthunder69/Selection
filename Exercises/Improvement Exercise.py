#joseph Everden
#selection improvement exercise
#25-09-14

month = 0
while month == 0:
    month = int(input("Please enter a month as a number between 1-12: "))
    if month == 1:
        print("The month you entered is January")
    if month == 2:
        print("The month you entered is February")
    if month == 3:
        print("The month you entered is March")
    if month == 4:
        print("The month you entered is April")
    if month == 5:
        print("The month you entered is May")
    if month == 6:
        print("The month you entered is June")
    if month == 7:
        print("The month you entered is July")
    if month == 8:
        print("The month you entered is August")
    if month == 9:
        print("The month you entered is September")
    if month == 10:
        print("The month you entered is October")
    if month == 11:
        print("The month you entered is November")
    if month == 12:
        print("The month you entered is December")
    if month > 12 or month < 1:
        print("You entered an invalid number!")
        print("Try again...")
        month = 0
