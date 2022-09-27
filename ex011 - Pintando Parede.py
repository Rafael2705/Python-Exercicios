lar = float(input('Largura da parede: '))
Alt = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e a sua área é de {:.2f}m²:'.format(lar, Alt, lar*Alt))
print('Para pintar essa parede você precisara de {}l de tinta'.format((lar*Alt)/2))
