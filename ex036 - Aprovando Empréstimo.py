casa = float(input('Valor da casa: R$'))
Salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento:'))
prestação = (casa / (anos * 12))
minimo = (Salario / 100) * 30
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos),end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')



