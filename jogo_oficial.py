#importação de bibliotecas
import pygame
import time
import random
pygame.init()
pygame.mixer.init()


#cria quadro principal do jogo
WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
cor_branca = (250, 250, 250)
cor_preta = (0, 0, 0)
pygame.display.set_caption('ARE YOU A GENIUS?')

