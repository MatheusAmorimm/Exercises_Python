expression = str(input("Digite a expressao: "))
pilha = []
for parenteses in expression:
    if parenteses == "(":
        pilha.append("(")
    elif parenteses == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressao esta montada corretamente!")
else:
    print("Sua expressao esta montada incorretamente!")