números = list()
while True:
    n = int(input('Digite um Valor:'))
    if n not in números:
        números.append(n)
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')
