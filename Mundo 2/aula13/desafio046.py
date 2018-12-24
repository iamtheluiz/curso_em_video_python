# imports
from time import sleep
import pygame

print("""
|******************|
|    Desafio046    |
|******************|
""")
print("Contagem Regressiva! (10 até 0)")

for count in range(10, -1, -1):
    print("{}!".format(count))
    sleep(1)

print("""
==================
 FELIZ ANO NOVO!!
==================
""")

print("~Som de Fogos~")
pygame.mixer.init()
pygame.mixer_music.load('desafio046.mp3')
pygame.mixer_music.set_volume(1)
pygame.mixer_music.play()
input("Terminar? ")
