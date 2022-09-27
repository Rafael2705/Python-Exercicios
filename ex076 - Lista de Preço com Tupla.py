listagem = ('Lápis',1.50,
            'Borracha', 1.00,
            'Caderno',21.00,
            'Estojo',25.00,
            'trasferidor',7,
            'Mochila',120.00,
            'canetas',10.50,
            'livros',34.90)
print('-'*40)
print(f'{"Listagem de preço":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)