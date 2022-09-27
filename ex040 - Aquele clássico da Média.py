n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, media))
if media >= 7:
    print('O aluno está \033[1;33;05mAprovado\033[m')
elif media < 5:
    print('O aluno está \033[1;31;05mReprovado\033[m')
else:
    print('O aluno está em \33[1;97mrecuperação\033[m')
