viagem = float(input('Qual é a distância de sua viagem? '))
print('Você está preste a começar uma viagem de {}km'.format(viagem))
if viagem <= 200:
    preço = viagem * 0.50
else:
   preço = viagem * 0.45
print('E o preco da sua passagem será de R${}'.format(preço))