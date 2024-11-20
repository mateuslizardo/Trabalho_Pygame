import pygame
from personagem import *

def batalha(herois):
    cont = 0
    maior_velocidade(herois)
    tela = desenha_batalha(herois)
    
    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

            desenha_batalha(herois)
            escrever_turno(herois, cont, tela)
            vida_personagens(herois, tela)

            pygame.time.delay(1000)

            if cont < 4:
                cont += 1
            elif cont == 4:
                cont = 0

def maior_velocidade(lista_personagens):
        return lista_personagens.sort(key=lambda personagem: personagem.velocidade, reverse=True)

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
    return tela

def escrever_turno(herois, cont, tela):
    fonte = pygame.font.SysFont('Inter', 48)

    if cont == 0:
        texto = fonte.render(f"{herois[0]}'s turn!", True, (255, 255, 255))
        tela.blit(texto, (112, 518))
        texto = fonte.render("attack", True, (255, 255, 255))
        tela.blit(texto, (112, 575))
        texto = fonte.render("defend", True, (255, 255, 255))
        tela.blit(texto, (420, 575))
        texto = fonte.render("insight", True, (255, 255, 255))
        tela.blit(texto, (112, 632))
        texto = fonte.render("skill", True, (255, 255, 255))
        tela.blit(texto, (420, 632))

    elif cont == 1:
        texto = fonte.render("Necromancer's turn!", True, (255, 255, 255))
        tela.blit(texto, (112, 518))

    elif cont == 2:
        texto = fonte.render(f"{herois[1]}'s turn!", True, (255, 255, 255))
        tela.blit(texto, (112, 518))
        tela.blit(texto, (112, 518))
        texto = fonte.render("attack", True, (255, 255, 255))
        tela.blit(texto, (112, 575))
        texto = fonte.render("defend", True, (255, 255, 255))
        tela.blit(texto, (420, 575))
        texto = fonte.render("insight", True, (255, 255, 255))
        tela.blit(texto, (112, 632))
        texto = fonte.render("skill", True, (255, 255, 255))
        tela.blit(texto, (420, 632))

    elif cont == 3:
        texto = fonte.render("Skeleton's turn!", True, (255, 255, 255))
        tela.blit(texto, (112, 518))

    elif cont == 4:
        texto = fonte.render(f"{herois[2]}'s turn!", True, (255, 255, 255))
        tela.blit(texto, (112, 518))
        tela.blit(texto, (112, 518))
        texto = fonte.render("attack", True, (255, 255, 255))
        tela.blit(texto, (112, 575))
        texto = fonte.render("defend", True, (255, 255, 255))
        tela.blit(texto, (420, 575))
        texto = fonte.render("insight", True, (255, 255, 255))
        tela.blit(texto, (112, 632))
        texto = fonte.render("skill", True, (255, 255, 255))
        tela.blit(texto, (420, 632))

    pygame.display.flip()

def vida_personagens(herois, tela):
    fonte = pygame.font.SysFont('Inter', 48)

    texto = fonte.render(f"{herois[0]}", True, (255, 255, 255))
    tela.blit(texto, (630, 518))
    
    texto = fonte.render(f"{herois[0].vida} / {herois[0].vida_inicial}", True, (255, 255, 255))
    tela.blit(texto, (788, 518))

    texto = fonte.render(f"{herois[1]}", True, (255, 255, 255))
    tela.blit(texto, (630, 575))
    
    texto = fonte.render(f"{herois[1].vida} / {herois[1].vida_inicial}", True, (255, 255, 255))
    tela.blit(texto, (788, 578))

    texto = fonte.render(f"{herois[2]}", True, (255, 255, 255))
    tela.blit(texto, (630, 632))
    
    texto = fonte.render(f"{herois[2].vida} / {herois[2].vida_inicial}", True, (255, 255, 255))
    tela.blit(texto, (786, 632))

    pygame.display.flip()