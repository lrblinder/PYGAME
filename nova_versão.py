import pygame
import time
import random
from random import randrange


pygame.init()
pygame.mixer.init()

WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
cor_branca = (250,250,250)
cor_preta = (0,0,0)
# window.fill(cor_branca)
pygame.display.set_caption('ARE YOU A GENIUS?')

font = pygame.font.SysFont(None, 70)
text = font.render('GAME OVER', True, (0, 0, 255))

# iniciar assets
tela_normal = pygame.image.load('quadrados/Cores iniciais.png')
tela_normal = pygame.transform.scale(tela_normal, (WIDTH, HEIGHT))

verde_ligado =pygame.image.load('quadrados_claros/Verde ligado.png')
verde_ligado = pygame.transform.scale(verde_ligado, (WIDTH, HEIGHT)) 


azul_ligado=pygame.image.load('quadrados_claros/Azul ligado.png')
azul_ligado= pygame.transform.scale(azul_ligado, (WIDTH, HEIGHT))

amarelo_ligado=pygame.image.load('quadrados_claros/Amarelo ligado.png')
amarelo_ligado= pygame.transform.scale(amarelo_ligado, (WIDTH, HEIGHT))

vermelho_ligado=pygame.image.load('quadrados_claros/Vermelho ligado.png')
vermelho_ligado= pygame.transform.scale(vermelho_ligado, (WIDTH, HEIGHT))

            

click_on_off = False
jogada_do_player = []

repeticao_cores=0
sequencia_jogo=[]
cont = 0
cores_escolhidas = 0
lista_cores_aleatorias = []

while True:

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            quit()
    
    #mouse
    #mouse= pygame.mouse.get_pos()
    #print(mouse) #mouse[0] = mouse no x e mouse[1] = mouse no y

    click = pygame.mouse.get_pressed()
    #print(click)

    # Sortear as cores
    if cores_escolhidas == len(lista_cores_aleatorias):
        numero = random.randint(0, 3)
        lista_cores_aleatorias.append(numero)
        print(lista_cores_aleatorias)

    # Imprimir as cores
        for cor in lista_cores_aleatorias:
            if cor == 0:
                # Amarelo
                window.blit(azul_ligado, (0,0)) # Imprimir o amarelo claro
                pygame.display.update() 
                time.sleep(1) # Esperar 3 segundos 
                window.blit(tela_normal, (0,0))# Imprimir o amarelo escuro
                pygame.display.update()
            elif cor == 1:
                # vermelho
                window.blit(vermelho_ligado, (0,0)) # Imprimir o amarelo claro
                pygame.display.update() 
                time.sleep(1) # Esperar 3 segundos 
                window.blit(tela_normal, (0,0)) # Imprimir o amarelo escuro
                pygame.display.update()
            elif cor == 2:
                # Verde
                window.blit(amarelo_ligado, (0,0)) # Imprimir o amarelo claro
                pygame.display.update() 
                time.sleep(1) # Esperar 3 segundos 
                window.blit(tela_normal, (0,0)) # Imprimir o amarelo escuro
                pygame.display.update()
            elif cor == 3:
                # Azul
                window.blit(verde_ligado, (0,0)) # Imprimir o amarelo claro
                pygame.display.update() 
                time.sleep(1) # Esperar 3 segundos 
                window.blit(tela_normal, (0,0)) # Imprimir o amarelo escuro
                pygame.display.update()
            time.sleep(1)
            
    
    n_cores = len(lista_cores_aleatorias)
    jogando = True
    mouse = (0,0)

    if jogando:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if mouse [0]>201 and mouse[0]<292 and mouse[1] < 520 and mouse[1]>360:
            if click[0]==False and click_on_off == True:
                cor = 2
                jogada_do_player.append(2)
                print(jogada_do_player)

                window.blit(amarelo_ligado, (0,0))#quadrado inferior esquerdo
                pygame.display.update()
                time.sleep(1)
                window.blit(tela_normal, (0,0))#quadrado inferior esquerdo
                pygame.display.update()

                # for i in range(len(lista_cores_aleatorias)):
                #     if lista_cores_aleatorias[i]!=jogada_do_player[i]:
                #         print("Game Over")
                #         window.blit(text, (85, 10))
                #         pygame.quit()
                #         quit()

                cores_escolhidas+=1

            if n_cores == cores_escolhidas:
                jogando = False
                time.sleep(2)
        
        if mouse [0]>305 and mouse[0]<396 and mouse[1]<520 and mouse[1]>360:
            if click[0]==False and click_on_off == True:
                cor = 3
                jogada_do_player .append(3)
                print(jogada_do_player)

                window.blit(verde_ligado, (0,0))#quadrado inferior direito
                pygame.display.update()
                time.sleep(1)
                window.blit(tela_normal, (0,0))#quadrado inferior esquerdo
                pygame.display.update()
                
                # for i in range(len(lista_cores_aleatorias)):
                #     if lista_cores_aleatorias[i]!=jogada_do_player[i]:
                #         print("Game Over")
                #         window.blit(text, (85, 10))
                #         pygame.quit()
                #         quit()

                cores_escolhidas+=1
            if n_cores == cores_escolhidas:
                jogando = False
                time.sleep(2)

        if mouse[0]>201 and mouse[0]<292 and mouse[1]<345 and mouse[1]>185:
            if click[0]==False and click_on_off == True:
                cor = 0
                jogada_do_player.append(0)
                print(jogada_do_player)

                window.blit(azul_ligado, (0,0))#quadrado superior esquerdo
                pygame.display.update()
                time.sleep(1)
                window.blit(tela_normal, (0,0))#quadrado inferior esquerdo
                pygame.display.update()

                # for i in range(len(lista_cores_aleatorias)):
                #     if lista_cores_aleatorias[i]!=jogada_do_player[i]:
                #         print("Game Over")
                #         window.blit(text, (85, 10))
                #         pygame.quit()
                #         quit()
                cores_escolhidas+=1
            if n_cores == cores_escolhidas:
                jogando = False
                time.sleep(2)
        
        if mouse[0]>305 and mouse[0]<396 and mouse[1]<345 and mouse[1]>185:
            if click[0]==False and click_on_off == True:
                cor = 1
                jogada_do_player.append(1)
                print(jogada_do_player)

                window.blit(vermelho_ligado, (0,0))#quadrado superior direito
                pygame.display.update()
                time.sleep(1)
                window.blit(tela_normal, (0,0))#quadrado inferior esquerdo
                pygame.display.update()

                # for i in range(len(lista_cores_aleatorias)):
                #     if lista_cores_aleatorias[i]!=jogada_do_player[i]:
                #         print("Game Over")
                #         window.blit(text, (85, 10))
                #         pygame.quit()
                #         quit()

                cores_escolhidas+=1
            if n_cores == cores_escolhidas:
                jogando = False
                time.sleep(2)
        click_on_off = click[0]
        jogada_do_player = []
    

        

    
    
    
