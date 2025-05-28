from time import sleep

colors = ('\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[7m')

def ajuda(comm):
    title(f'Acessando o manual do comando \'{comm}\'', 4)
    print(colors[6], end='')
    help(comm)
    print(colors[0], end='')
    sleep(2)

def title(msg, cor=0):
    tam = len(msg) + 4
    print(colors[cor], end='')
    print('~'* tam)
    print(f' {msg}')
    print('~'* tam)
    print(colors[0], end='')
    sleep(1)

comando= ""
while True:
    title('Sistema de Ajuda PyHelp', 2)
    comando = str(input("Function ou Lib > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
title('Ate Logo!', 1)