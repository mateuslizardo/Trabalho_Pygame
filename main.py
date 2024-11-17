from personagem import *
import pygame
from tela_inicial import *

paladin = Personagem(0, 0, 0, 0, "paladin")
rogue = Personagem(0, 0, 0, 0, "rogue")
wizard = Personagem(0, 0, 0, 0, "wizard")
hunter = Personagem(0, 0, 0, 0, "hunter")
priest = Personagem(0, 0, 0, 0, "priest")

lista_personagens = [paladin, rogue, wizard, hunter, priest]

pygame.init()
pygame.font.init()
tela = pygame.display.set_mode((1024, 768))
background = pygame.image.load("imagens/teste 3 ps.png")

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        
        herois = selecao(lista_personagens)
        print(f"{herois[0], herois[1], herois[2]}")