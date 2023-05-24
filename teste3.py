import pygame

pygame.init()
pygame.mixer.init()

WIDTH = 600
HEIGHT = 700
LADO = 250
window = pygame.display.set_mode((WIDTH, HEIGHT))
cor_branca = (250,250,250)
window.fill(cor_branca)
pygame.display.set_caption('ARE YOU A GENIUS?')

font = pygame.font.SysFont(None, 70)
text = font.render('ARE YOU A', True, (0, 0, 0))
text2 = font.render('GENIUS', True, (0, 0, 255))

# iniciar assets
# assets = {}
verde_ligado =pygame.image.load('quadrados/quadrado verde claro.png').convert_alpha()
verde_ligado = pygame.transform.scale(verde_ligado, (LADO, LADO)) 
verde_desligado=pygame.image.load('quadrados/quadrado verde escuro.png').convert_alpha()
verde_desligado= pygame.transform.scale(verde_desligado, (LADO, LADO))
azul_desligado=pygame.image.load('quadrados/quadrado azul escuro.png').convert_alpha()
azul_desligado= pygame.transform.scale(azul_desligado, (LADO, LADO))
azul_ligado=pygame.image.load('quadrados/quadrado azul claro.png').convert_alpha()
azul_ligado= pygame.transform.scale(azul_ligado, (LADO, LADO))
amarelo_desligado=pygame.image.load('quadrados/amarelo escuro.png').convert_alpha()
amarelo_desligado = pygame.transform.scale(amarelo_desligado, (LADO, LADO))
amarelo_ligado=pygame.image.load('quadrados/amarelo claro.jpg').convert_alpha()
amarelo_ligado= pygame.transform.scale(amarelo_ligado, (LADO, LADO))
vermelho_desligado=pygame.image.load('quadrados/vermelho escuro.jpg').convert_alpha()
vermelho_desligado= pygame.transform.scale(vermelho_desligado, (LADO, LADO))
vermelho_ligado=pygame.image.load('quadrados/vermelho claro.jpg').convert_alpha()
vermelho_ligado= pygame.transform.scale(vermelho_ligado, (LADO, LADO))

# def desenho_inicio(window):
#     window.blit(verde_desligado, (50, 150))
#     pygame.display.update()



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


while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            quit()
    
    window.blit(text, (85, 10))
    window.blit(text2, (375, 10))
    pygame.display.update()


    #mouse
    mouse= pygame.mouse.get_pos()
    print(mouse) #mouse[0] = mouse no x e mouse[1] = mouse no y

    if mouse [0]>50 and mouse[0]<300 and mouse[1] < 650 and mouse[1]>400:
        window.blit(amarelo_ligado, (50, 400))#quadrado inferior esquerdo
    elif mouse [0]>300 and mouse[0]<550 and mouse[1]<650 and mouse[1]>400:
        window.blit(azul_ligado, (300, 400))#quadrado inferior direito
    elif mouse[0]>50 and mouse[0]<300 and mouse[1]<400 and mouse[1]>150:
        window.blit(verde_ligado, (50, 150))#quadrado superior esquerdo
    elif mouse[0]>300 and mouse[0]<550 and mouse[1]<400 and mouse[1]>150:
        window.blit(vermelho_ligado, (300, 150))#quadrado superior direito
