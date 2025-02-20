number = float(input("Enter the first number: "))
secNumber = float(input("Another number: "))
bigger = number

if secNumber > number:
    bigger = secNumber
    print("The second number is bigger")
elif number == secNumber:
    print("The number are equal")
else:
    print("The first number is bigger")