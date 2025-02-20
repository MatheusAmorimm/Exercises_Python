firstNumber = float(input("Enter a number: "))
secNumber = float(input("Other number: "))
thirdNumber = float(input("Last number: "))

smallest = firstNumber
bigger = secNumber

if secNumber < firstNumber and secNumber < thirdNumber:
    smallest = secNumber
if thirdNumber < firstNumber and thirdNumber < secNumber:
    smallest = thirdNumber

if firstNumber > secNumber and firstNumber > thirdNumber:
    bigger = firstNumber
if thirdNumber > secNumber and thirdNumber > firstNumber:
    bigger = thirdNumber

print('The smallest is: {}'. format(smallest))
print('And, the bigger number is: {}'.format(bigger))