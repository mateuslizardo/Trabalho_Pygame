import pygame
from personagem import *

def batalha(herois):
    desenha_batalha(herois)

    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

def desenha_batalha(herois):
    tela = pygame.display.set_mode((1024, 768))
    background = pygame.image.load("imagens/Batalha.png")
    tela.blit(background, (0, 0))
    

    heroi0 = pygame.image.load(herois[0].imagem)
    heroi0 = pygame.transform.scale(heroi0, (124, 124))
    heroi1 = pygame.image.load(herois[1].imagem)
    heroi1 = pygame.transform.scale(heroi1, (124, 124))
    heroi2 = pygame.image.load(herois[2].imagem)
    heroi2 = pygame.transform.scale(heroi2, (124, 124))

    tela.blit(heroi0, (221, 160))
    tela.blit(heroi1, (110, 269))
    tela.blit(heroi2, (221, 360))
    pygame.display.flip()