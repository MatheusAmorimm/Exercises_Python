from time import sleep
housePrice = float(input('How many the house you want buy? R$ '))
salary = float(input('What`s your salary? R$'))
years = int(input("In how many years? ")) * 12
valueInstallments = housePrice / years

print("\033[1;35mCalculating whether we can finance this ...\033[m")
sleep(1)

if valueInstallments > salary * 0.3:
    print("\033[1;31mSorry, we can`t finance this property for you. The installments exceed 30% of your salary\033[m")
else:
    print("\033[1;32mCongratulations! We can finvb ance this property!\033[m")