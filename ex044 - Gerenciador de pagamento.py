preço = float(input('Preço das Compras: R$ '))
print('''Formas de pagamento
[ 1 ] á vista dinheiro
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a sua opção? '))
if opção == 1:
    total = preço - (preço / 100 * 10)
elif opção == 2:
    total = preço - (preço / 100 * 5)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço/100*20)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Suas compras será parcelada em {}x de R${:.2f}'.format(totparc, parcela))
else:
    total = preço
    print('Opção Inválida')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))

