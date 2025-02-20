firstNumber = int(input("say me a random number: "))
doubleNumber = firstNumber * 2
tripleNumber = firstNumber * 3
squareRoot = firstNumber**(1/2) #ou pode ser pow(firstNumber, (1/2))

print("Your double is {} \nYour triple is {} \nAnd your square root is {:.2f}".format(doubleNumber, tripleNumber, squareRoot))