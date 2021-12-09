print('===== DESAFIO 19 =====')
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

print('\n--- MODO 2---')
from random import choice
n1 = str(input('nome do Primeiro aluno: '))
n2 = str(input('nome do Segundo aluno: '))
n3 = str(input('nome doTerceiro aluno: '))
n4 = str(input('nome do Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido para isso foi {}'.format(escolhido))
