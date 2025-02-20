print('=' * 25)
print('Sequencia de Fibonacci')
print('=' * 25)

numberOfTerms = int(input("Qauntos termos deseja mostrar? "))
termo1 = 0
termo2 = 1
sequencia = 3
print('{} -> {} -> '.format(termo1, termo2), end='')

while sequencia <= numberOfTerms:
    termo3 = termo1 + termo2
    print('{} -> '.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    sequencia += 1

print("Fim")