# imports
import pygame

print("|*****************|")
print("|    Desafio21    |")
print("|*****************|")
print("")
print("MP3 Player")

pygame.mixer.init()
pygame.mixer.music.load("d21.mp3")
pygame.mixer.music.play()

input("Digite algo para parar: ")
