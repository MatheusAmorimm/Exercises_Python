from datetime import date

olderMan = " "
olderManAge = 0
womansAbove20 = 0
curretYear = date.today().year
contAge = 0

for p in range(1,5):
    print("----- {}º PESSOA -----".format(p))
    name = str(input("Whats your name? "))
    age = int(input("Whats year old? "))
    sex = str(input("How do you identify? M or F: ")).strip().upper()

    contAge += age

    if p == 1:
        olderManAge = age
    else:
        if age > olderManAge:
            olderManAge = age

    if sex == 'F' and age < 20:
        womansAbove20 += 1
    if sex == 'M' and age == olderManAge:
        olderMan = name

print("""O homem mais velho e: {} e tem {} anos
{} mulheres tem menos de 20 anos
Media de idade {} """.format(olderMan, olderManAge, womansAbove20, contAge / 4))