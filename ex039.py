import datetime

currentDate = datetime.date.today()
currentYear = currentDate.year
yearOfBirth = int(input("What year were you born? "))
enlistment = currentYear - yearOfBirth

if enlistment < 18:
    print("{} year left until military enlistment".format(18 - enlistment))
elif enlistment == 18:
    print("You must enlist now!")
else:
    print("It`s been {} years since your enlistment".format(enlistment - 18))