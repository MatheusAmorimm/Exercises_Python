height = float(input("How high the wall is in metre? "))
width = float(input("And, what is the width is in metre? "))
area = height * width
quantPaintNeed = area / 2

print("Your wall have {} square metres and needs {} liters of paint".format(area, quantPaintNeed))