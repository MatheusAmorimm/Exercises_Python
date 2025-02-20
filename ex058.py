import random
from time import sleep
sortedNumber = random.randint(0,10)

print('\033[1;33m-*-' * 25)
print('\033[mLet`s go play! I think of a number between 0 and 10. And you try to guess!')
print('\033[1;35mThinking...')
print('\033[1;33m-*-' * 25)
sleep(1)

contador = 1
userResponse = 11
while userResponse != sortedNumber:
    userResponse = int(input("\033[mWhat number you think it is? "))
    if userResponse == sortedNumber:
        print('\033[1;32mOh my God! You hit my number right! Congratss!!!\033[m')
        print('For the win, you took {} attempts'.format(contador))
    else:
        if userResponse > sortedNumber:
            print('\033[1;31mLess... Try Again\033[m')
        elif userResponse < sortedNumber:
            print('\033[1;31mMore.. Try Again\033[m')
        contador += 1
