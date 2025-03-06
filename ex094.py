pessoa = {}
pessoas = []
totalidade = 0
media = 0
mulheres = []

while True:
    pessoa["nome"] = str(input("Nome: "))
    pessoa["sexo"] = str(input("Sexo [M/F]: ")).strip().upper()[0]
    while pessoa["sexo"] != "M" and pessoa["sexo"] != "F":
        pessoa["sexo"] = str(input("Opcao Invalida. Sexo [M/F]: ")).strip().upper()[0]
    if pessoa["sexo"] == "F":
        mulheres.append(pessoa.copy())
    pessoa["idade"] = int(input("Quantos anos voce tem? "))
    totalidade += pessoa["idade"]
    pessoas.append(pessoa.copy())
    del pessoa["nome"]
    del pessoa["sexo"]
    del pessoa["idade"]
    resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    while resposta != "N" and resposta != "S":
        resposta = str(input("Tente novamente. Deseja continuar? [S/N] ")).strip().upper()[0]
    if resposta == "N":
        break

media = totalidade / len(pessoas)
print(f"- Foram cadastradas {len(pessoas)} pessoas")
print(f"- A media de idade do grupo e: {media:.2f}")
print(f"- Dessas pessoas cadastradas, as mulheres sao: ", end="")
for indice, nome in enumerate(mulheres):
    print(mulheres[indice]["nome"], end=" ")
print()

