kilometers = float(input('How many kilometers is your trip? '))

if kilometers <= 200:
    payment = kilometers * 0.5
    print("You must pay R${}". format(payment))
else:
    payment = kilometers * 0.45
    print("You must pay R${}".format(payment))