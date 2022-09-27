from time import sleep
print('='*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
print('='*10)
decimo = primeiro + (10 - 1) * razão
for n in range(primeiro, decimo + razão, razão):
    print(n, end=' - ')
    sleep(0.5)
print('Acabou')