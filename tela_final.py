from personagem import *
import pygame

#Imprime as imagens de vitória ou derrota
def resultado(herois, venceu):
    tela = pygame.display.set_mode((1024, 768))
    if venceu == True:
        img = pygame.image.load("imagens/tela final vitoria.png")
        tela.blit(img, (0, 0))
        #Coloca os personagens escolhidos na tela
        personagem1 = pygame.image.load(herois[0].link_imagem())
        personagem1 = pygame.transform.scale(personagem1, (200, 200))
        personagem2 = pygame.image.load(herois[1].link_imagem())
        personagem2 = pygame.transform.scale(personagem2, (200, 200))
        personagem3 = pygame.image.load(herois[2].link_imagem())
        personagem3 = pygame.transform.scale(personagem3, (200, 200))
        tela.blit(personagem1, (177, 310))
        tela.blit(personagem2, (377, 310))
        tela.blit(personagem3, (601, 310))

        pygame.display.flip()

    else:
        img = pygame.image.load("imagens/tela final derrota.png")
        tela.blit(img, (0, 0))

        pygame.display.flip()

    pygame.time.delay(10000)