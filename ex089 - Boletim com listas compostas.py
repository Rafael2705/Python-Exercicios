ficha = []
while True:
    nome =str(input('nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    print('-' * 60)
    opc = int(input('Mostrar nota de qual Aluno? (999 Interrompe): '))
    if opc == 999:
        print('Finalizando')
        break
    if opc <= len(ficha) :
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< Volte Sempre >>>')


