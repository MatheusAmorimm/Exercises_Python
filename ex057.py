sex = " "
while sex != "M" and sex != 'F':
    sex = str(input("Qual seu sexo? [M/F] ")).strip().upper()[0]
    if sex != 'M' and sex != 'F':
        print("Sexo invalido, insira novamente.")
print('Obrigado!')
