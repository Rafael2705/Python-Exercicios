cont = ('zero', 'um','dois','três','quatro','Cinco',
        'seis','sete','oito','Nove','Dez',
        'Onze','Doze','Treze','Quatorze','Quinze',
        'Dezesseis','Dezessete','Dezoito', 'Dezenove','Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.,',end='')
print(f'Você digitou o número {cont[num]}')