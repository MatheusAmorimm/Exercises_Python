import random

firstStudant = str(input("Which a first studant? "))
secondStudant = str(input("Now, a second: "))
thirdStudant = str(input("Third studant: "))
fourthStudant = str(input("Fourth studant: "))

list_of_apresentation = random.sample([firstStudant, secondStudant, thirdStudant, fourthStudant], k=4)

print("The order on for the apresentation is: {}". format(list_of_apresentation))