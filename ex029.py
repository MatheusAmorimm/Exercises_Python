print('Welcome to Detran system!')
velocity = int(input('What is the curent speed of your car? '))

if velocity > 80:
   penalty = (velocity - 80) * 7
   print('\033[1;30;41mYou should pay R${:.2f} for the your traffic fine!\033[m'.format(penalty))
else:
    print('\033[1;30;42mYou don`t made a traffic fine!\033[m')
print("\033[1;34mHave a good day, drive safely\033[m")