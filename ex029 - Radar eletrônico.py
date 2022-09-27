print('-=-'*14)
velocidade = float(input('Em que velocidade você está dirigindo?'))
if velocidade > 80:
    print('-=-' * 20)
    print('Multado você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80)*7
    print('Você deve pagar uma multa de R${}'.format(multa))
print('-=-'*20)
print('Tenha um bom dia! Dirija com segurança!')
