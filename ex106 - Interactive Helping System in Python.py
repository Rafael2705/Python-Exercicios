from time import sleep

c = ('\033[m',  # 0 sem cor
     '\033[0;30;41m',  # 1 Vermelho
     '\033[0;30;42m',  # 2 Amarelo
     '\033[0;30;43m',  # 3 Azul
     '\033[0;30;44m',  # 4 Roxo
     '\033[0;30;45m',  # 5 Roxo
     '\033[7;30m'  # 6 branco
     )


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[5], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input("função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até Logo!!!', 1)
