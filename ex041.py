from datetime import date

currentDt = date.today()
currentYr = currentDt.year
yearOfBirth = int(input("What year were born? "))
category = currentYr - yearOfBirth

if category <= 9:
    print("Your category is Mirim")
elif category <= 14:
    print("Your category is Infantil")
elif category <= 19:
    print("Your category is Junior")
elif category <= 25:
    print("Your category is Senior")
else:
    print("Your a master!")