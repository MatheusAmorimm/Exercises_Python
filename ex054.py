from datetime import date
pessoasMenores = 0
pessoasMaiores = 0
currentyear = date.today()

for c in range(1,8):
    anoNasc = int(input("Em que ano a {}º pessoa nasceu? ".format(c)))
    if currentyear.year - anoNasc < 21:
        pessoasMenores += 1
    else:
        pessoasMaiores += 1

print("Menores: {} - Maiores: {}".format(pessoasMenores, pessoasMaiores))