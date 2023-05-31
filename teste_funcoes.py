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


#música
simon_sound=pygame.mixer.Sound("sons/button.mp3")

game_over = pygame.image.load('fotos gerais/on (3).png')
game_over = pygame.transform.scale(game_over, (WIDTH, HEIGHT))

tela_instrucoes = pygame.image.load('fotos gerais/on (4).png')
tela_instrucoes = pygame.transform.scale(tela_instrucoes, (WIDTH, HEIGHT))

tela_inicial = pygame.image.load('fotos gerais/on (1).png')
tela_inicial = pygame.transform.scale(tela_inicial, (WIDTH, HEIGHT))

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

def display_menu():
    window.blit(tela_inicial, (0,0))
    pygame.display.update()

def instrucoes():
    window.blit(tela_instrucoes, (0,0))
    pygame.display.update()

def pisca_cor(cor):
    window.blit(cor, (0, 0))
    simon_sound.play()

def jogada_do_jogador(cor_ascender,num_cor):
    jogada_do_player.append(num_cor)
    window.blit(cor_ascender, (0, 0))
    simon_sound.play()
    pygame.display.update()
    time.sleep(1)
    window.blit(tela_normal, (0, 0))
    pygame.display.update()

def tela_game_over():
    window.blit(game_over, (20, 0))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()
    
game_state = "menu"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    if game_state == "menu":
        display_menu()
        mouse_menu = pygame.mouse.get_pos()
        click_menu = pygame.mouse.get_pressed()

        if mouse_menu[0] > 190 and mouse_menu[0] < 410 and mouse_menu[1] < 369 and mouse_menu[1] > 251:
            if click_menu[0] == True:
                game_state = "jogando"
                
        if mouse_menu[0] > 190 and mouse_menu[0] < 410 and mouse_menu[1] < 522 and mouse_menu[1] > 404:
            if click_menu[0] == True:
                game_state = "instruções"
                

    elif game_state == "instruções":
        instrucoes()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(mouse)
        if mouse[0] > 433 and mouse[0] < 575 and mouse[1] < 580 and mouse[1] > 503:
            if click[0] == True:
                game_state = "menu"

    elif game_state == "jogando":
        time.sleep(2)
        if cores_escolhidas == len(lista_cores_aleatorias):
            numero = random.randint(0, 3)
            lista_cores_aleatorias.append(numero)

            for cor in lista_cores_aleatorias:
                if cor == 0:
                    pisca_cor(azul_ligado)
                elif cor == 1:
                    pisca_cor(vermelho_ligado)
                elif cor == 2:
                    pisca_cor(amarelo_ligado)
                elif cor == 3:
                    pisca_cor(verde_ligado)
                    
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
                        jogada_do_jogador(amarelo_ligado, cor)
                        cores_escolhidas += 1

                if mouse[0] > 305 and mouse[0] < 396 and mouse[1] < 520 and mouse[1] > 360:
                    if click[0] == True:
                        cor = 3
                        jogada_do_jogador(verde_ligado, cor)
                        cores_escolhidas += 1

                if mouse[0] > 201 and mouse[0] < 292 and mouse[1] < 345 and mouse[1] > 185:
                    if click[0] == True:
                        cor = 0
                        jogada_do_jogador(azul_ligado, cor)
                        cores_escolhidas += 1

                if mouse[0] > 305 and mouse[0] < 396 and mouse[1] < 345 and mouse[1] > 185:
                    if click[0] == True:
                        cor = 1
                        jogada_do_jogador(vermelho_ligado, cor)
                        cores_escolhidas += 1

                i = 0
                while i < len(jogada_do_player):
                    if jogada_do_player[i] != lista_cores_aleatorias[i]:
                        tela_game_over()
                    i += 1

                if cores_escolhidas == len(lista_cores_aleatorias):
                    if jogada_do_player != lista_cores_aleatorias:
                        tela_game_over()
                    
                    else:
                        time.sleep(1)
                        cores_escolhidas = 0
                        jogada_do_player = []
                        lista_cores_aleatorias.append(random.randint(0, 3))
                        print(lista_cores_aleatorias)
                        for cor in lista_cores_aleatorias:
                            if cor == 0:
                                window.blit(azul_ligado, (0, 0))
                                simon_sound.play()
                            elif cor == 1:
                                window.blit(vermelho_ligado, (0, 0))
                                simon_sound.play()
                            elif cor == 2:
                                window.blit(amarelo_ligado, (0, 0))
                                simon_sound.play()
                            elif cor == 3:
                                window.blit(verde_ligado, (0, 0))
                                simon_sound.play()
                            pygame.display.update()
                            time.sleep(1)
                            window.blit(tela_normal, (0, 0))
                            pygame.display.update()
                            time.sleep(1)