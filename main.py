from personagem import *
import pygame
from tela_inicial import *

paladin = Personagem(0, 0, 0, 0)
rogue = Personagem(0, 0, 0, 0)
wizard = Personagem(0, 0, 0, 0)
hunter = Personagem(0, 0, 0, 0)
priest = Personagem(0, 0, 0, 0)

lista_personagens = [paladin, rogue, wizard, hunter, priest]

pygame.init()
tela = pygame.display.set_mode((1024, 768))
background = pygame.image.load("imagens/teste 3 ps.png")

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        
        tela.blit(background, (0, 0))
        pygame.display.flip()
        herois = selecao(lista_personagens)