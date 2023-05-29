import pygame
import time
import random

pygame.init()
pygame.mixer.init()

WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
cor_branca = (250, 250, 250)
cor_preta = (0, 0, 0)
pygame.display.set_caption('ARE YOU A GENIUS?')

font = pygame.font.SysFont(None, 70)
text = font.render('GAME OVER', True, (0, 0, 255))

tela_normal = pygame.image.load('quadrados/Cores iniciais.png')
tela_normal = pygame.transform.scale(tela_normal, (WIDTH, HEIGHT))

verde_ligado = pygame.image.load('quadrados_claros/Verde ligado.png')
verde_ligado = pygame.transform.scale(verde_ligado, (WIDTH, HEIGHT))

azul_ligado = pygame.image.load('quadrados_claros/Azul ligado.png')
azul_ligado = pygame.transform.scale(azul_ligado, (WIDTH, HEIGHT))

amarelo_ligado = pygame.image.load('quadrados_claros/Amarelo ligado.png')
amarelo_ligado = pygame.transform.scale(amarelo_ligado, (WIDTH, HEIGHT))

vermelho_ligado = pygame.image.load('quadrados_claros/Vermelho ligado.png')
vermelho_ligado = pygame.transform.scale(vermelho_ligado, (WIDTH, HEIGHT))

jogada_do_player = []
sequencia_jogo = []
cores_escolhidas = 0
lista_cores_aleatorias = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if cores_escolhidas == len(lista_cores_aleatorias):
        numero = random.randint(0, 3)
        lista_cores_aleatorias.append(numero)
        print(lista_cores_aleatorias)

        for cor in lista_cores_aleatorias:
            if cor == 0:
                window.blit(azul_ligado, (0, 0))
                
            elif cor == 1:
                window.blit(vermelho_ligado, (0, 0))
                
            elif cor == 2:
                window.blit(amarelo_ligado, (0, 0))
                

            elif cor == 3:
                window.blit(verde_ligado, (0, 0))
                
            pygame.display.update()
            time.sleep(1)
            window.blit(tela_normal, (0, 0))
            pygame.display.update()
            time.sleep(1)
            


        jogando = True
        while jogando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if mouse[0] > 201 and mouse[0] < 292 and mouse[1] < 520 and mouse[1] > 360:
                if click[0] == True:
                    cor = 2
                    jogada_do_player.append(2)
                    print(jogada_do_player)
                    window.blit(amarelo_ligado, (0, 0))
                    pygame.display.update()
                    time.sleep(1)
                    window.blit(tela_normal, (0, 0))
                    pygame.display.update()
                    cores_escolhidas += 1

            if mouse[0] > 305 and mouse[0] < 396 and mouse[1] < 520 and mouse[1] > 360:
                if click[0] == True:
                    cor = 3
                    jogada_do_player.append(3)
                    print(jogada_do_player)
                    window.blit(verde_ligado, (0, 0))
                    pygame.display.update()
                    time.sleep(1)
                    window.blit(tela_normal, (0, 0))
                    pygame.display.update()
                    cores_escolhidas += 1

            if mouse[0] > 201 and mouse[0] < 292 and mouse[1] < 345 and mouse[1] > 185:
                if click[0] == True:
                    cor = 0
                    jogada_do_player.append(0)
                    print(jogada_do_player)
                    window.blit(azul_ligado, (0, 0))
                    pygame.display.update()
                    time.sleep(1)
                    window.blit(tela_normal, (0, 0))
                    pygame.display.update()
                    cores_escolhidas += 1

            if mouse[0] > 305 and mouse[0] < 396 and mouse[1] < 345 and mouse[1] > 185:
                if click[0] == True:
                    cor = 1
                    jogada_do_player.append(1)
                    print(jogada_do_player)
                    window.blit(vermelho_ligado, (0, 0))
                    pygame.display.update()
                    time.sleep(1)
                    window.blit(tela_normal, (0, 0))
                    pygame.display.update()
                    cores_escolhidas += 1

            i = 0
            while i < len(jogada_do_player):
                if jogada_do_player[i] != lista_cores_aleatorias[i]:
                    print("Game Over")
                    window.blit(text, (85, 10))
                    pygame.display.update()
                    time.sleep(2)
                    pygame.quit()
                    quit()
                i += 1

            if cores_escolhidas == len(lista_cores_aleatorias):
                if jogada_do_player != lista_cores_aleatorias:
                    print("Game Over")
                    window.blit(text, (85, 10))
                    pygame.display.update()
                    time.sleep(2)
                    pygame.quit()
                    quit()
                
                else:
                    cores_escolhidas = 0
                    jogada_do_player = []
                    lista_cores_aleatorias.append(random.randint(0, 3))
                    print(lista_cores_aleatorias)
                    for cor in lista_cores_aleatorias:
                        if cor == 0:
                            window.blit(azul_ligado, (0, 0))
                        elif cor == 1:
                            window.blit(vermelho_ligado, (0, 0))
                        elif cor == 2:
                            window.blit(amarelo_ligado, (0, 0))
                        elif cor == 3:
                            window.blit(verde_ligado, (0, 0))
                        pygame.display.update()
                        time.sleep(1)
                        window.blit(tela_normal, (0, 0))
                        pygame.display.update()
                        time.sleep(1)
                