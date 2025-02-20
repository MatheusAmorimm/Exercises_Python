palavras = "APRENDER", "PROGRAMAR", "PYTHON", "LINGUAGEM", "CURSO", "GRATIS", "ESTUDAR", "PRATICAR", "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO"

for p in palavras:
    print(f"\nNa palavra {p} temos as vogais", end=" ")
    for letra in p:
        if letra in "AEIOU":
            print(f"{letra}", end=" ")