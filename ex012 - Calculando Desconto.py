pre = float(input('Qual é o preço do produto? R$'))
Des = float(input('O valor do desconto? %'))
print('O produto que custava {:.2f}, na promoção com desconto de {:.2f}% vai custar R${:.2f}:'.format(pre, Des, (pre-(pre / 100 * Des))))