from personagem import *
import pygame
from tela_inicial import *

paladin = Personagem()
rogue = Personagem()
wizard = Personagem()
hunter = Personagem()
priest = Personagem()

lista_personagens = [paladin, rogue, wizard, hunter, priest]

pygame.init()
tela = pygame.display.set_mode(1024, 768)

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        
        herois = selecao(lista_personagens)