n1 = int(input('Primeiro valor'))
n2 = int(input('Segundo Valor'))
opção = 0
while opção != 5:
    print('''    [ 1 ] soma
    [ 2 ] multiplicação
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
        soma = n1 +n2
        print('=-=' * 10)
        print('A soma entre {} e {} é {}'. format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('=-=' * 10)
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print('=-=' * 10)
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('=-=' * 10)
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        elif n1 == n2:
            print('=-=' * 10)
            print('Os dois valores são iguais')

    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor'))
        n2 = int(input('Segundo Valor'))

    elif opção == 5:
        print('=-=' * 10)
        print('Finalizando. . . .')
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)
print('Fim do programa! Volte Sempre!')

