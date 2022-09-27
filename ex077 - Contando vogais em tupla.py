palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'ESTUDAR', 'PRATICAR', 'TRABALHAR'
            'MERCADO', 'PROGRAMADOR', 'FUTURO',)
for p in palavras:
    print(f'\nNa plavra {p.upper()} temos', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')