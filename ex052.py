number = int(input("Inside a number: "))
total = 0

for c in range(1, number + 1):
    if number % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

print('\033[m\nO numero {} foi divisel {} vezes'. format(number, total))
if total == 2:
    print("O numero e primo!")
else:
    print("O numero nao e primo!")
