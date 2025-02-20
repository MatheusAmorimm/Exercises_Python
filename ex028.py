import random
from time import sleep
sortedNumber = random.randint(0,5)

print('\033[1;33m-*-' * 25)
print('\033[mLet`s go play! I think of a number between 0 and 5. And you try to guess!')
print('\033[1;35mThinking...')
print('\033[1;33m-*-' * 25)
sleep(1)
userResponse = int(input("\033[mWhat number you think it is? "))

if userResponse == sortedNumber:
    print("\033[1;30;42mWow, you're correct! Congrats!\033[m")
else:
    print("\033[1;30;41mHahaha! I win, you didn't get it right!\033[m")