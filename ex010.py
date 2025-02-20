brazilianMoney = float(input("How much R$ your have? R$"))
convertToDol = brazilianMoney / 6.04
convertToEuro = brazilianMoney / 6.22

print("Then, you have {:.2f} dollars and {:.2f} euros".format(convertToDol, convertToEuro))