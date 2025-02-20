firstNote = float(input("What`s your first note? "))
secNote = float(input("Enter your second note: "))
average = (firstNote + secNote) / 2

if average < 5:
    print("You are rejected")
elif 5 <= average <= 6.9:
    print("You are in recuperation")
elif average >= 7:
    print("You are approved")