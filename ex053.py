phrase = str(input("Digite uma frase: ")).strip().upper()
words = phrase.split()
together = ''.join(words)
inverse = ''
'''
inverse = together[::-1] // da pra usar dessa maneira
'''
for letter in range(len(together) - 1, -1, -1):
    inverse += together[letter]
print('o inverso de {} e {}'.format(together, inverse))
if inverse != together:
    print('Nao e um palindromo!')
else:
    print('E um palindromo')
