from random import randint
from time import sleep
pc = randint(0, 5)  # código sortear 1 número entre 0 á 5
print('-=-'*18)
print('Vou pensar em um número entre 0 a 5, tente advinhar...')
print('-=-'*18)
jogador = int(input('Em que número eu pensei?'))
print('Processando. . .')
sleep(3)
if jogador == pc:
    print('Parabéns!!!! Você conseguiu me vencer!!!')
else:
    print('Ganhei! Eu pensei no numero {} e não no {}'.format(pc, jogador))
