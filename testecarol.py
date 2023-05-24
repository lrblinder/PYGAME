import pygame

pygame.init()
pygame.mixer.init()

WIDTH = 700
HEIGHT = 700
LADO = 100
window = pygame.display.set_mode((WIDTH, HEIGHT))
cor_branca = (250,250,250)
window.fill(cor_branca)
pygame.display.set_caption('ARE YOU A GENIUS?')

verde = pygame.image.load('quadrados/quadrado verde claro.png').convert_alpha()






# iniciar assets
# assets = {}
# assets['verde_ligado']=pygame.image.load('quadrados/quadrado verde claro.png').convert_alpha()
# assets['verde_ligado'] = pygame.transform.scale(assets['verde_ligado'], (LADO, LADO))
# assets['verde_desligado']=pygame.image.load('quadrados/quadrado verde escuro.png').convert_alpha()
# assets['verde_desligado'] = pygame.transform.scale(assets['verde_desligado'], (LADO, LADO))
# assets['azul_desligado']=pygame.image.load('quadrados/quadrado azul escuro.png').convert_alpha()
# assets['azul_desligado'] = pygame.transform.scale(assets['azul_desligado'], (LADO, LADO))
# assets['azul_ligado']=pygame.image.load('quadrados/quadrado azul claro.png').convert_alpha()
# assets['azul_ligado'] = pygame.transform.scale(assets['azul_ligado'], (LADO, LADO))
# assets['amarelo_desligado']=pygame.image.load('quadrados/amarelo escuro.png').convert_alpha()
# assets['amarelo_desligado'] = pygame.transform.scale(assets['amarelo_desligado'], (LADO, LADO))
# assets['amarelo_ligado']=pygame.image.load('quadrados/amarelo claro.jpg').convert_alpha()
# assets['amarelo_ligado'] = pygame.transform.scale(assets['amarelo_ligado'], (LADO, LADO))
# assets['vermelho_desligado']=pygame.image.load('quadrados/vermelho escuro.jpg').convert_alpha()
# assets['vermelho_desligado'] = pygame.transform.scale(assets['vermelho_desligado'], (LADO, LADO))
# assets['vermelho_ligado']=pygame.image.load('quadrados/vermelho claro.jpg').convert_alpha()
# assets['vermelho_ligado'] = pygame.transform.scale(assets['vermelho_ligado'], (LADO, LADO))



# class Cores(pygame.sprite.Sprite):
#     def image(self,groups,assets):
#         pass


# while True:
#     for event in pygame.event.get():
#         if event.type== pygame.QUIT:
#             pygame.quit()
#             quit()
#     pygame.display.update()


#     #mouse
#     mouse= pygame.mouse.get_pos()
#     print(mouse)