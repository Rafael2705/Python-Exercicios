print('-=-'*10)
print('-=-Analisador de triangulos-=-')
print('-=-'*10)
r1 = float(input('Primeiro seguimento '))
r2 = float(input('Segundo seguimento '))
r3 = float(input('Terceiro seguimento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('OS seguimentos acima PODEM formar o triangulo! ',end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('OS seguimentos acima  Não PODEM formar o triangulo!')