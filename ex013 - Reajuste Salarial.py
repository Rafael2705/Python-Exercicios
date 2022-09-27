sal = float(input('Qual é o salário do funcionário? R$'))
au = float(input('Quantos porcento de aumento %'))
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}:'.format(sal, au,sal+(sal/100*au)))
