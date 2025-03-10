aluno = dict()
aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input(f"Qual a media de {aluno["nome"]}? "))
if aluno["media"] < 5.00:
    aluno["situacao"] = "Reprovado"
elif 5 <= aluno["media"] < 7.0:
    aluno["situacao"] = "Recuperacao"
else:
    aluno["situacao"] = "Aprovado"
for chave, valor in aluno.items():
    print(f"{chave} e igual a {valor}")
