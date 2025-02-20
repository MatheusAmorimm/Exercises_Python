number = int(input("Enter a integer number to know your multiplication table: "))

for c in range (0, 11):
    print('{} x {:2} = {}'.format(number, c, number * c ))

