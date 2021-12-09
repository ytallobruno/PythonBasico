print('=== Quer calcular seu IMC (Indice de massa corporal)? ===')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
res = peso/(altura*altura)
print('seu IMC é igual a: {:.2f}'.format(res))
if 24.9 >= int(res) >= 18.5:
    print('Parabéns! Você está dentro da faixa ideal')
else:
    print('Voce tem que cuidar mais de sua saúde !')

print('O ideal é estar entre 18.5 e 24.9.')
