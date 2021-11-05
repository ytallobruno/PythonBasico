print('===== DESAFIO 12 =====')
n1 = float(input('Qual o preço do produto? '))
d = n1 - (n1 * 0.05)
p = n1 + (n1 * 0.10)

print('Olha que sorte! \nEsse produto à vista com nosso desconto sai por {:.2f}'.format(d))
print('Mas a prazo ele sai por {:.2f}'.format(p))
