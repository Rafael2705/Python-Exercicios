salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    atual = ((salario/100)*15)+salario
else:
    atual = ((salario/100)*10)+salario

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, atual))