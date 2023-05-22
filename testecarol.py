import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('ARE YOU A GENIUS?')


# iniciar assets
LADO=100

assets = {}
assets['verde_ligado']=pygame.image.load('C:\Users\lrbli\Downloads\PYGAME\png verde claro.png').convert_alpha()
assets['verde_ligado'] = pygame.transform.scale(assets['verde_ligado'], (LADO, LADO))
assets['verde_desligado']=pygame.image.load('C:\Users\lrbli\Downloads\PYGAME\png verde claro.png').convert_alpha()
assets['verde_desligado'] = pygame.transform.scale(assets['verde_desligado'], (LADO, LADO))
assets['azul_desligado']=pygame.image.load('C:\Users\lrbli\Downloads\PYGAME\png verde claro.png').convert_alpha()
assets['azul_desligado'] = pygame.transform.scale(assets['azul_desligado'], (LADO, LADO))
assets['azul_ligado']=pygame.image.load('C:\Users\lrbli\Downloads\PYGAME\png verde claro.png').convert_alpha()
assets['azul_ligado'] = pygame.transform.scale(assets['azul_ligado'], (LADO, LADO))
assets['amarelo_desligado']=pygame.image.load('C:\Users\lrbli\Downloads\PYGAME\png verde claro.png').convert_alpha()
assets['amarelo_desligado'] = pygame.transform.scale(assets['amarelo_desligado'], (LADO, LADO))
assets['amarelo_ligado']=pygame.image.load('C:\Users\lrbli\Downloads\PYGAME\png verde claro.png').convert_alpha()
assets['amarelo_ligado'] = pygame.transform.scale(assets['amarelo_ligado'], (LADO, LADO))
assets['vermelho_desligado']=pygame.image.load('C:\Users\lrbli\Downloads\PYGAME\png verde claro.png').convert_alpha()
assets['vermelho_desligado'] = pygame.transform.scale(assets['vermelho_desligado'], (LADO, LADO))
assets['vermelho_ligado']=pygame.image.load('C:\Users\lrbli\Downloads\PYGAME\png verde claro.png').convert_alpha()
assets['vermelho_ligado'] = pygame.transform.scale(assets['vermelho_ligado'], (LADO, LADO))

# Carrega os sons do jogo
pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
pygame.mixer.music.set_volume(0.4)
assets['light_on_soun'] = pygame.mixer.Sound('')
assets['destroy_sound'] = pygame.mixer.Sound('assets/snd/expl6.wav')
assets['pew_sound'] = pygame.mixer.Sound('assets/snd/pew.wav')




class Cores(pygame.sprite.Sprite):
    def image(self,groups,assets):






    while True:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

        #mouse
        mouse= pygame.mouse.get_pos()
        print(mouse)