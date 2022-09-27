from time import sleep


def contador(i, f, p):
    print('-=~=-' * 8)
    print(f'Contador de {i} até {f} de {p} em {p}')
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM')
    print('-=~=-' * 8)


# programa principal
contador(0, 100, 10)
contador(10, 0, 2)
print('-=~=-' * 8)
print('Agora é a sua vez de personalizar a contagem')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
