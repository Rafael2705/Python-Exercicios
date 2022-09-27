times = ('América-MG', 'Athletico ',' Atlético-GO', 'Atlético-MG','Avaí',
         'Botafogo' , 'Ceará', 'Corinthians', 'Coritiba', 'Cuiabá',
         'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional',
         'Juventude', 'Palmeiras', 'Red Bull Bragantino', 'Santos', 'São Paulo')
print('-*-'*30)
print(f'Lista de time: {times}')
print('-*-'*30)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-*-'*30)
print(f'Os 4 últimos são: {times}[-4:]')
print('-*-'*30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-*-'*30)
print(f'São Paulo está na {times.index("São Paulo")+1}° posição')
print('-*-'*30)