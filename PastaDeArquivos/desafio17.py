print('===== DESAFIO 17 =====')
print('=== FAZENDO NORMAL ===')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A Hipotenusa vai medir {:.2f}'.format(hi))


import math
print('\n=== IMPORTANDO MATH ===')
cat1 = float(input('Comprimento do primeiro cateto: '))
cat2 = float(input('Comprimento do segundo cateto: '))
res = math.hypot(cat1, cat2)
print('A Hipotenusa desse triângulo-retângulo será {:.2f}'.format(res))


from math import hypot
print('\n=== IMPORTANDO HYPOT DO MATH ===')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A Hipotenusa será {:.2f}'.format(hi))
