firstTerm = int(input('insert a first term of the PA: '))
ratio = int(input('What is the ration for arithmetic progession? '))
contador = 1

while contador != 10:
    firstTerm += ratio
    contador += 1
    print(firstTerm)