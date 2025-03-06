from datetime import date
pessoa = {}
pessoa["nome"] = str(input("Nome: "))
anoAtual = date.today().year
anoNasc = int(input("Qual sua data de nascimento? "))
pessoa["idade"] = anoAtual - anoNasc
pessoa["ctps"] = int(input("Nº da Carteira de Trabalho [0 se nao tiver]: "))
if pessoa["ctps"] == 0:
    print("-*" * 25)
    for chave, valor in pessoa.items():
        print(f"{chave} tem o valor {valor}")
else:
    pessoa["contribuicao"] = int(input("Ano de contratacao: "))
    pessoa["salario"] = float(input("Salario: "))
    anoAposentadoria = pessoa["contribuicao"] + 35
    pessoa["aposentadoria"] = anoAposentadoria - anoNasc
    print("-*" * 25)
    for chave, valor in pessoa.items():
        print(f"{chave} tem o valor {valor}")
