aluno = dict()
aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input(f"Qual a media de {aluno["nome"]}? "))
if aluno["media"] < 7.0:
    aluno["situacao"] = "Reprovado"
else:
    aluno["situacao"] = "Aprovado"
for chave, valor in aluno.items():
    print(f"{chave} e igual a {valor}")
