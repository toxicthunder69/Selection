#test grading program

testScore = int(input("Please enter your test score: "))
if testScore > 40 and testScore <= 50:
    print("E grade")
if testScore > 50 and testScore <= 60:
    print("D grade")
if testScore > 60 and testScore <= 70:
    print("C grade")
if testScore > 70 and testScore <= 80:
    print("B grade")
if testScore > 80:
    print("A grade")
if testScore < 40:
    print("Fail")
