import random
from time import sleep
print("-"*40)
print("{:^40}".format("SORTEIO DE JOGOS DA MEGA-SENA"))
print("-"*40)
jogos = list()
numsort = list()
valor = 0

qtd_jogos = int(input("Quantos jogos voce quer sortear? "))
print("{:-^40}".format(f" SORTEANDO {qtd_jogos} JOGOS "))
for jogo in range(0, qtd_jogos):
    while len(numsort) < 6:
        valor = random.randint(1,60)
        if valor not in numsort:
            numsort.append(valor)
    numsort.sort()
    jogos.append(numsort[:])
    numsort.clear()

for qtd, jogo in enumerate(jogos):
    print(f"Jogo {qtd+1}: {jogo}")
    sleep(1)
    qtd+=1
print("{:-^40}".format(" BOA SORTE "))