from time import sleep

ficha = list()

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input("Tem mais alunos para adicionar? [S/N] ")).strip().upper()[0]
    while resposta != "S" and resposta != "N":
        resposta = str(input("Opcao invalida, tente novamente. Deseja continuar? [S/N] ")).strip().upper()[0]
    if resposta == "N":
        break
print("-" * 26)
print(f"{"Nº":<4}{"Nome":<10}{"Media":>8}")
print("-" * 26)
for indice, aluno in enumerate(ficha):
    print(f"{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")

while True:
    print("-" * 30)
    aluno = int(input("Deseja ver as notas de qual aluno? [Digite o Nº do aluno, caso queira sair, digite 999]: "))
    while aluno not in ficha:
        aluno = int(input("Opcao invalida, tente novamente. Lembre-se deve colocar o numero respectivo do aluno que deseja ver."))
    if aluno == 999:
        print("Finalizando...")
        sleep(1)
        break
    if aluno <= len(ficha) - 1:
        print(f"Notas de {ficha[aluno][0]} sao {ficha[aluno][1]} ")