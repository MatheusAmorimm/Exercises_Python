from time import sleep

mulherMenor = 0
homens = 0
maioresDeIdade = 0

print("{:=^40}".format(" CADASTRO "))
while True:
    idade = int(input("Idade: "))
    sex = str(input("Sexo: [M/F] ")).strip().upper()[0]
    while sex != "M" and sex != "F":
        sex = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if idade < 20 and sex == "F":
        mulherMenor += 1
    if idade > 18:
        maioresDeIdade += 1
    if sex == "M":
        homens += 1
    print("*" * 20)
    continuar = str(input("Quer cadastrar outra pessoa? [S/N] ")).strip().upper()[0]
    while continuar != "S" and continuar != "N":
        continuar = str(input("Quer cadastrar outra pessoa? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
    print("*" * 20)
print("Analisando...")
sleep(1)
print("*" * 20)
print(f"""Mulheres com menos de 20 anos: {mulherMenor}
Homes cadastrados: {homens}
Pessoas maiores de 18 anos: {maioresDeIdade}""")