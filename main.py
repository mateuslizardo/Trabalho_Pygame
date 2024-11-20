from personagem import *
import pygame
import tela_inicial
import batalha

paladin = Personagem(200, 0, 0, 1, "paladin", "imagens/Paladino.png", 200)
rogue = Personagem(80, 0, 0, 2, "rogue", "imagens/rogue.png", 80)
wizard = Personagem(80, 0, 0, 3, "wizard", "imagens/wizardfinal 2.png", 80)
hunter = Personagem(200, 0, 0, 4, "hunter", "imagens/hunter sprite.png", 200)
priest = Personagem(200, 0, 0, 5, "priest", "imagens/PRIEST_Shadow.png", 200)

lista_personagens = [paladin, rogue, wizard, hunter, priest]

pygame.init()
pygame.font.init()

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        
        herois = tela_inicial.selecao(lista_personagens)
        batalha.batalha(herois)