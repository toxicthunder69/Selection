#Joseph Everden
#01/10/14
#Month Selection

month_input = int(input("Enter a number between 1 and 12 to represent a month: "))
if month_input == 1:
    print("You entered the month as January.")
if month_input == 2:
    print("You entered the month as February.")
if month_input == 3:
    print("You entered the month as March.")
if month_input == 4:
    print("You entered the month as April.")
if month_input == 5:
    print("You entered the month as May.")
if month_input == 6:
    print("You entered the month as June.")
if month_input == 7:
    print("You entered the month as July.")
if month_input == 8:
    print("You entered the month as August.")
if month_input == 9:
    print("You entered the month as September.")
if month_input == 10:
    print("You entered the month as October.")
if month_input == 11:
    print("You entered the month as November.")
if month_input == 12:
    print("You entered the month as December.")
if month_input <= 0 or month_input > 12:
    print("You entered an invalid number!")
