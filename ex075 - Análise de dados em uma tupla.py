num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite último número: ')))
print(f'Você digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
       print(f'O valor 3 apareceu na {num.index(3)+1}° possição')
else:
       print('o valor 3 não foi digitado em nenhuma possição')
print('Os valores pares digitados foram ',end='')
for n in num:
       if n % 2 == 0:
              print(n, end='')