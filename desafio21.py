print('===== DESAFIO 21 =====')
'''import pygame
pygame.init()
pygame.mixer.music.load('desafio21.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

print('--- MODO 2---')
from pygame import mixer
mixer.init()
mixer.music.load('desafio21.mp3')
mixer.music.play()
input('Agora você escuta?')