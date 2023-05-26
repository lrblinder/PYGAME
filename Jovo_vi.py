import pygame
import time
import random
from random import randrange

# Iniciar o jogo 
pygame.init()
pygame.mixer.init()

WIDTH = 600
HEIGHT = 700
LADO = 250
window = pygame.display.set_mode((WIDTH, HEIGHT))
cor_branca = (250,250,250)
cor_preta = (0,0,0)
window.fill(cor_branca)
pygame.display.set_caption('ARE YOU A GENIUS?')

font = pygame.font.SysFont(None, 70)
text = font.render('ARE YOU A', True, (0, 0, 0))
text2 = font.render('GENIUS', True, (0, 0, 255))

pygame.draw.rect(window, cor_preta, (40, 140, 520, 520), 10)

# iniciar assets
# assets = {}

verde_ligado =pygame.image.load('quadrados_claros/quadrado verde claro.png').convert_alpha()
verde_ligado = pygame.transform.scale(verde_ligado, (LADO, LADO)) 
verde_desligado=pygame.image.load('quadrados/quadrado verde escuro.png').convert_alpha()
verde_desligado= pygame.transform.scale(verde_desligado, (LADO, LADO))
azul_desligado=pygame.image.load('quadrados/quadrado azul escuro.png').convert_alpha()
azul_desligado= pygame.transform.scale(azul_desligado, (LADO, LADO))
azul_ligado=pygame.image.load('quadrados_claros/quadrado azul claro.png').convert_alpha()
azul_ligado= pygame.transform.scale(azul_ligado, (LADO, LADO))
amarelo_desligado=pygame.image.load('quadrados/amarelo escuro.png').convert_alpha()
amarelo_desligado = pygame.transform.scale(amarelo_desligado, (LADO, LADO))
amarelo_ligado=pygame.image.load('quadrados_claros/amarelo claro.jpg').convert_alpha()
amarelo_ligado= pygame.transform.scale(amarelo_ligado, (LADO, LADO))
vermelho_desligado=pygame.image.load('quadrados/vermelho escuro.jpg').convert_alpha()
vermelho_desligado= pygame.transform.scale(vermelho_desligado, (LADO, LADO))
vermelho_ligado=pygame.image.load('quadrados_claros/vermelho claro.jpg').convert_alpha()
vermelho_ligado= pygame.transform.scale(vermelho_ligado, (LADO, LADO))


click_on_off = False
jogada_do_player = []

repeticao_cores=0
sequencia_jogo=[]
cont = 0
k = 0

# Definir a lista de cores aleatórias
lista_cores_aleatorias = []

# def verifica_clique():
#     if mouse[0]>50 and mouse[0]<300 and mouse[1] < 650 and mouse[1]>400:
#             lista_jogadas.append(0)
#             quantidade_de_jogadas += 1
#             if quantidade_de_n == quantidade_de_jogadas:
#                 jogadas = False
#             if mouse [0]>300 and mouse[0]<550 and mouse[1]<650 and mouse[1]>400:
#                 lista_jogadas.append(0)
#                 quantidade_de_jogadas += 1
#                 if quantidade_de_n == quantidade_de_jogadas:
#                     jogadas = False
#             if mouse[0]>50 and mouse[0]<300 and mouse[1]<400 and mouse[1]>150:
#                 lista_jogadas.append(0)
#                 quantidade_de_jogadas += 1
#                 if quantidade_de_n == quantidade_de_jogadas:
#                     jogadas = False
#             if mouse[0]>50 and mouse[0]<300 and mouse[1]<400 and mouse[1]>150:
#                 lista_jogadas.append(0)
#                 quantidade_de_jogadas += 1
#                 if quantidade_de_n == quantidade_de_jogadas:
#                     jogadas = False
#             if mouse[0]>300 and mouse[0]<550 and mouse[1]<400 and mouse[1]>150:
#                 lista_jogadas.append(0)
#                 quantidade_de_jogadas += 1
#                 if quantidade_de_n == quantidade_de_jogadas:
#                     jogadas = False
# # Estrutura do jogo ------------------------------------------------------------------------------------------------------------------
# while True:
#     for event in pygame.event.get():
#         if event.type== pygame.QUIT:
#             pygame.quit()
#             quit()
    
#     window.blit(text, (85, 10))
#     window.blit(text2, (375, 10))
    

#     #mouse
#     mouse= pygame.mouse.get_pos()
#     #print(mouse) #mouse[0] = mouse no x e mouse[1] = mouse no y

#     click = pygame.mouse.get_pressed()
    #print(click)

    # if mouse [0]>50 and mouse[0]<300 and mouse[1] < 650 and mouse[1]>400:
    #     window.blit(amarelo_ligado, (50, 400))#quadrado inferior esquerdo
    #     if click[0]==False and click_on_off == True:
    #         jogada_do_player.append(2)
    #         print(jogada_do_player)
    # else:
    #     window.blit(amarelo_desligado, (50, 400))
    
    # if mouse [0]>300 and mouse[0]<550 and mouse[1]<650 and mouse[1]>400:
    #     window.blit(azul_ligado, (300, 400))#quadrado inferior direito
    #     if click[0]==False and click_on_off == True:
    #         jogada_do_player .append(3)
    #         print(jogada_do_player)
    # else:
    #     window.blit(azul_desligado, (300, 400))
    
    # if mouse[0]>50 and mouse[0]<300 and mouse[1]<400 and mouse[1]>150:
    #     window.blit(verde_ligado, (50, 150))#quadrado superior esquerdo
    #     if click[0]==False and click_on_off == True:
    #         jogada_do_player.append(0)
    #         print(jogada_do_player)
    # else:
    #     window.blit(verde_desligado, (50, 150))
    # if mouse[0]>300 and mouse[0]<550 and mouse[1]<400 and mouse[1]>150:
    #     window.blit(vermelho_ligado, (300, 150))#quadrado superior direito
    #     if click[0]==False and click_on_off == True:
    #         jogada_do_player.append(1)
    #         print(jogada_do_player)
    # else:
    #     window.blit(vermelho_desligado, (300, 150))
    # cont+=1
    # click_on_off = click[0]

    # pygame.display.update()


    # Gerar uma lista com cores aleatórias
    lista_cores_aleatorias = []


    # Imprimir as cores
while True:
    for cor in lista_cores_aleatorias:
        if cor == 0:
            # Amarelo
            window.blit(amarelo_ligado, (50, 400)) # Imprimir o amarelo claro
            pygame.display.update() 
            time.sleep(3) # Esperar 3 segundos 
            window.blit(amarelo_desligado, (50, 400))# Imprimir o amarelo escuro
            pygame.display.update()
        elif cor == 1:
            # vermelho
            window.blit(vermelho_ligado, (300, 150)) # Imprimir o amarelo claro
            pygame.display.update() 
            time.sleep(3) # Esperar 3 segundos 
            window.blit(vermelho_ligado, (300, 150)) # Imprimir o amarelo escuro
            pygame.display.update()
        elif cor == 2:
            # Verde
            window.blit(vermelho_ligado, (300, 150)) # Imprimir o amarelo claro
            pygame.display.update() 
            time.sleep(3) # Esperar 3 segundos 
            window.blit(vermelho_ligado, (300, 150)) # Imprimir o amarelo escuro
            pygame.display.update()
        elif cor == 3:
            # Azul
            window.blit(azul_ligado, (300, 400)) # Imprimir o amarelo claro
            pygame.display.update() 
            time.sleep(3) # Esperar 3 segundos 
            window.blit(azul_ligado, (300, 400)) # Imprimir o amarelo escuro
            pygame.display.update()
        time.sleep(3)
        print('terminou')

    # Jogador joga 
    # lista_jogadas = []
    # jogadas = True
    # quantidade_de_n = len(lista_cores_aleatorias)
    # quantidade_de_jogadas = 0
    # while jogadas:
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         mouse = pygame.mouse.get_pos()
    #     # Pegue o clik e adicione na lista 
            


    # # Você verifica se o jogador acertou a ordem 
    # if lista_jogadas != lista_cores_aleatorias:
    #     print("Você perdeu")

