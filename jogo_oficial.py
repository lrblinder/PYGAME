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

#música
simon_sound=pygame.mixer.Sound("sons/button.mp3")

#faz upload imagem game over
game_over = pygame.image.load('fotos gerais/on (3).png')
game_over = pygame.transform.scale(game_over, (WIDTH, HEIGHT))

#faz upload tela instruções
tela_instrucoes = pygame.image.load('fotos gerais/on (4).png')
tela_instrucoes = pygame.transform.scale(tela_instrucoes, (WIDTH, HEIGHT))

#faz upload tela inicial
tela_inicial = pygame.image.load('fotos gerais/on (1).png')
tela_inicial = pygame.transform.scale(tela_inicial, (WIDTH, HEIGHT))

#faz upload tela principal
tela_normal = pygame.image.load('quadrados/Cores iniciais.png')
tela_normal = pygame.transform.scale(tela_normal, (WIDTH, HEIGHT))

#faz upload do quadrado verde quando ligado
verde_ligado = pygame.image.load('quadrados_claros/Verde ligado.png')
verde_ligado = pygame.transform.scale(verde_ligado, (WIDTH, HEIGHT))

#faz upload do quadrado azul quando ligado
azul_ligado = pygame.image.load('quadrados_claros/Azul ligado.png')
azul_ligado = pygame.transform.scale(azul_ligado, (WIDTH, HEIGHT))

#faz upload do quadrado amarelo quando ligado
amarelo_ligado = pygame.image.load('quadrados_claros/Amarelo ligado.png')
amarelo_ligado = pygame.transform.scale(amarelo_ligado, (WIDTH, HEIGHT))

##faz upload do quadrado vermelho quando ligado
vermelho_ligado = pygame.image.load('quadrados_claros/Vermelho ligado.png')
vermelho_ligado = pygame.transform.scale(vermelho_ligado, (WIDTH, HEIGHT))

#cria variáveis fora do loop do jogo para preenchê-las durante o joo
jogada_do_player = []
sequencia_jogo = []
cores_escolhidas = 0
lista_cores_aleatorias = []

#cria função do menu
def display_menu():
    window.blit(tela_inicial, (0,0))
    pygame.display.update()

#cria função das instruções
def instrucoes():
    window.blit(tela_instrucoes, (0,0))
    pygame.display.update()

#cria função que pisca a cor
def pisca_cor(cor):
    window.blit(cor, (0, 0))
    simon_sound.play()

#cria função da jogada do player
def jogada_do_jogador(cor_ascender,num_cor):
    jogada_do_player.append(num_cor)
    window.blit(cor_ascender, (0, 0))
    simon_sound.play()
    pygame.display.update()
    time.sleep(1)
    window.blit(tela_normal, (0, 0))
    pygame.display.update()

#cria a função da tela final "game over"
def tela_game_over():
    window.blit(game_over, (20, 0))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

game_state = "menu" #define status do jogo

#INICIA LOOP PRINCIPAL DO JOGO
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    #VERIFICA CONDIÇÃO E ABRE A TELA DO MENU:
    if game_state == "menu":
        display_menu()
        mouse_menu = pygame.mouse.get_pos()
        click_menu = pygame.mouse.get_pressed()

        #VERIFICA ONDE O JOGADOR VAI CLICAR
        if mouse_menu[0] > 190 and mouse_menu[0] < 410 and mouse_menu[1] < 369 and mouse_menu[1] > 251:
            if click_menu[0] == True:
                game_state = "jogando" #se o jogador clicar no botão "jogar" atualiza o status do jogo para "jogando"
                
        if mouse_menu[0] > 190 and mouse_menu[0] < 410 and mouse_menu[1] < 522 and mouse_menu[1] > 404:
            if click_menu[0] == True:
                game_state = "instruções" #se o jogador clicar no botão "instruções" atualiza o status do jogo para "innstruções"
    
    # VERIFICA CONDIÇÃO E ABRE A TELA INSTRUÇÕES:
    elif game_state == "instruções":
        instrucoes()
        mouse = pygame.mouse.get_pos() #inicializa o mouse
        click = pygame.mouse.get_pressed() #inicializa o click
        
        if mouse[0] > 433 and mouse[0] < 575 and mouse[1] < 580 and mouse[1] > 503:
            if click[0] == True:
                game_state = "menu" #se o jogador clicar no botão "menu" atualiza o status do jogo para "menu"

    #VERIFICA CONDIÇÃO E ABRE A TELA DO JOGO:
    elif game_state == "jogando":
        time.sleep(2)
        if cores_escolhidas == len(lista_cores_aleatorias): #verifica se está na hora de sortear uma cor nova
            numero = random.randint(0, 3) #sorteia uma cor aleatória
            lista_cores_aleatorias.append(numero) #adiciona o número correspondente à cor aleatória na lista 
            #LOOP QUE FAZ AS CORES PISCAREM (percorre a lista de cores aleatórias e corresponde cada número da lista a uma cor, inserindo uma nova tela)
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
                time.sleep(0.8)
                window.blit(tela_normal, (0, 0))
                pygame.display.update()
                time.sleep(0.8)

            jogando = True
            #LOOP DA JOGADA DO JOGADOR
            while jogando:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                mouse = pygame.mouse.get_pos() #inicializa mouse
                click = pygame.mouse.get_pressed() #inicializa click

                #CHECA SE O CLICK FOI NO BOTÃO DE COR AMARELA
                if mouse[0] > 201 and mouse[0] < 292 and mouse[1] < 520 and mouse[1] > 360:
                    if click[0] == True:
                        cor = 2
                        jogada_do_jogador(amarelo_ligado, cor) #coloca imagem do amarelo piscando
                        cores_escolhidas += 1

                #CHECA SE O CLICK FOI NO BOTÃO DE COR VERDE
                if mouse[0] > 305 and mouse[0] < 396 and mouse[1] < 520 and mouse[1] > 360:
                    if click[0] == True:
                        cor = 3
                        jogada_do_jogador(verde_ligado, cor) #coloca imagem do verde piscando
                        cores_escolhidas += 1
                
                #CHECA SE O CLICK FOI NO BOTÃO DE COR AZUL
                if mouse[0] > 201 and mouse[0] < 292 and mouse[1] < 345 and mouse[1] > 185:
                    if click[0] == True:
                        cor = 0
                        jogada_do_jogador(azul_ligado, cor) #coloca imagem do azul piscando
                        cores_escolhidas += 1

                #CHECA SE O CLICK FOI NO BOTÃO DE COR VERMELHA
                if mouse[0] > 305 and mouse[0] < 396 and mouse[1] < 345 and mouse[1] > 185:
                    if click[0] == True:
                        cor = 1
                        jogada_do_jogador(vermelho_ligado, cor) #coloca imagem do vermelho piscando
                        cores_escolhidas += 1