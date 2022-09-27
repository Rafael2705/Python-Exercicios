from time import sleep
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11, 1):
    print('{} x {} = {}'.format(num, c, num * c))
    sleep(0.5)
print('Acabou')