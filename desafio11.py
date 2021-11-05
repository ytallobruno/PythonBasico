print('===== DESAFIO 11 =====')
n1 = float(input('Qual a altura da parede? '))
n2 = float(input('Qual a largura da parede? '))

a = n1 * n2
t = a / 2

print('\n A área da parede é {:.2} m²  \n logo, a quantidade de tinta necessária para pinta-lá é {:.2} litros/2m²'.format(a,t))
