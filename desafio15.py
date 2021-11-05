print('===== DESAFIO 15 =====')
n1 = float(input('Por quantos dias o carro foi alugado? '))
n2 = float(input('Por quantos kilometros rodou? '))

d = n1 * 60
k = n2 * 0.15

print('O valor por dia é R${:.2f} e por km R${:.2f},\n o valor total a ser pago é igual a R${:.2f}'.format(d,k,(d+k)))
