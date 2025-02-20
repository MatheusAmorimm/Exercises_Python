import math

angle = float(input("Which angle you wanna know? "))
rad = math.radians(angle)
sen = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)

print("The sine, cosine and tangent of {}, are respectively {:.2f}, {:.2f} and {:.2f}". format(angle, sen, cos, tang))