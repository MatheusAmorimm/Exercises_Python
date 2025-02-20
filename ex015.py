print("Hi! Good Afternoon! Lets go calculate your car rent!")

quantityDays = int(input("Say me, how many days did you use the car? "))
quantityKm = float(input("Now, how many kilometers did you drive the car? "))
finalValue = (quantityDays * 60) + (quantityKm * 0.15)

print("Then, your rent was worth R${:.2f}". format(finalValue))