print('===== DESAFIO 18 =====')
print('=== MODO 1 ===')
import math

an = float(input('Digite algum ângulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O seno desse angulo é {:.2f}, o cosseno é {:.2f} e a tangente {:.2f}'.format(sen, cos, tan))

print('\n=== MODO 2 ===')
from math import radians, sin, cos, tan
an = float(input('Digite um ângulo: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('Sendo assim, o seno é {:.2f}, o cosseno {:.2f} e a tangente {:.2f}'.format(sen, cos, tan))
