weight = float(input("How many kilos do you weigh? "))
height = float(input("In meters, how tall are you? "))
imc = weight / (height ** 2)

if imc < 18.5:
    print("Underweight")
elif 18.5 <= imc < 25:
    print("Ideal weight")
elif 25 <= imc < 30:
    print("Overweight")
elif 30 <= imc < 40:
    print("Obesity")
else:
    print("Morbid obesity")