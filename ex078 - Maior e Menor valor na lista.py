listanun = []
for c in range(0, 5):
    listanun.append(int(input(f'Digite um valor para o Posição {c +1} :')))
    if c == 0:
        mai = men = listanun[c]
    else:
        if listanun[c] > mai:
            mai = listanun[c]
        if listanun[c] < men:
            men = listanun[c]
print('=-'*30)
print(f'Você digitou os valores {listanun}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanun):
    if v == mai:
        print(f'{i+1}...', end='')
print()
print(f'O menor valor digitdo foi {men} nas posições ', end='')
for i, v in enumerate(listanun):
    if v == men:
        print(f'{i+1}...',end='')
print()