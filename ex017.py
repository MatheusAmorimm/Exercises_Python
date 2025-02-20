import math

cathet_opposite = float(input("Enter the lenght of the opposite side: "))
cathet_adj = float(input("Now, enter the lenght of the adjacent: "))

hypotenuse = math.hypot(cathet_opposite, cathet_adj)

print("The hypotenuse is: {:.2f}".format(hypotenuse))