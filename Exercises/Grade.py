#Joseph Everden
#01/10/14
#Exam Grade

grade = int(input("Enter you exam mark: "))
if grade <= 40:
    print("You achieved grade U.")
if grade > 40 and grade <= 50:
    print("You achieved grade E.")
if grade > 50 and grade <= 60:
    print("You achieved grade D.")
if grade > 60 and grade <= 70:
    print("You achieved grade C.")
if grade > 70 and grade <= 80:
    print("You achieved grade B.")
if grade > 80 and grade <= 100:
    print("You achieved grade A.")
if grade > 100:
    print("You can't get higher than 100.")
