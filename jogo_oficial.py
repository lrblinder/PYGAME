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

