from personagem import *
import pygame
import tela_inicial
import batalha

paladin = Personagem(0, 0, 0, 0, "paladin", "imagens/Paladino.png")
rogue = Personagem(0, 0, 0, 0, "rogue", "imagens/rogue.png")
wizard = Personagem(0, 0, 0, 0, "wizard", "imagens/wizardfinal 2.png")
hunter = Personagem(0, 0, 0, 0, "hunter", "imagens/hunter sprite.png")
priest = Personagem(0, 0, 0, 0, "priest", "imagens/PRIEST_Shadow.png")

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