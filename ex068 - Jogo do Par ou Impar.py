from random import randint
v = 0
while True:
    print('-' * 25)
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = str(input('Par ou Impar [P/I]')).strip().upper()
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]')).strip().upper()
    print(f'Você jogou {jogador} e o computador jogou {computador}.Total de {total}')
    print('Deu Par' if total % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            v += 1
            print('-' * 25)
        else:
            print('Você perdeu')
            break
        print('-' * 25)
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você ganhou!')
            v += 1
            print('-' * 25)
        else:
            print('Você perdeu')
            break
        print('-' * 25)

