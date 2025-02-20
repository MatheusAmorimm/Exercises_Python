"""import random

sort = random.choice(["Matheus", "jeniffer", "Lucas", "Braddock"])

print("The selected studant was: {}".format(sort))"""

import random

first = str(input("First Studant: "))
second = str(input("Second Studant: "))
third = str(input("Third Studant: "))
fourth = str(input("Fourth Studant: "))

sortedList = [first, second, third, fourth]

sortedStudant = random.choice(sortedList)

print("The selected studant is: {}".format(sortedStudant))
