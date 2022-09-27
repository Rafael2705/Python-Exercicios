peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso Ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')


