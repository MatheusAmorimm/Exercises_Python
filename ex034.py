salary = float(input("What`s your current salary? "))

if salary >= 1250:
    newSalary = (salary * 0.1) + salary
    print("Your new salary is: R${:.2f}".format(newSalary))
else:
    newSalary = (salary * 0.15) + salary
    print("Your new salary is R${:.2f}".format(newSalary))
