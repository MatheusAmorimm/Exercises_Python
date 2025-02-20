from time import sleep
productValue = float(input("How many the product? R$ "))
paymentCondition = int(input("""
1 - Boleto ou pix - 10% discount
2 - Credit Card 1x - 5% discount
3 - Credit Card 2x
4 - Credit Card 3x or more - 20% interest
What`s your choice?: """))

print("\033[1;35mProcessing...\033[m")
sleep(1)

if paymentCondition == 1:
    payment = productValue - (productValue * 0.1)
    print("You must pay R${:.2f}".format(payment))
elif paymentCondition == 2:
    payment = productValue - (productValue * 0.05)
    print("You must pay R${:.2f}".format(payment))
elif paymentCondition == 3:
    print("You must pay R${:.2f}, 2 installments of R$ {:.2f}".format(productValue, productValue / 2))
elif paymentCondition == 4:
    productInstallment = int(input("How many installments? "))
    payment = productValue + (productValue * 0.2)
    totalOfInstallments = payment / productInstallment
    print("You must pay R${:.2f}, {} installments of R$ {:.2f}".format(payment, productInstallment, totalOfInstallments))
else:
    print("\033[1;31mOps! You entered an invalid option. Try again!\033[m")