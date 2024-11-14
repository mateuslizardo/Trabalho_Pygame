import pygame
def selecao(lista_personagens):
    indice = 0
    personagens_selecionados = []

    bloco = pygame.image.load("imagens/introcomp_menu.png")
    bloco = pygame.transform.scale2x(bloco)
    paladin = pygame.image.load("imagens/Paladino.png")
    paladin = pygame.transform.scale2x(paladin)
    rogue = pygame.image.load("imagens/rogue.png")
    rogue = pygame.transform.scale2x(rogue)
    wizard = pygame.image.load("imagens/wizardfinal.png")
    wizard = pygame.transform.scale2x(wizard)
    hunter = pygame.image.load("imagens/hunter sprite.png")
    hunter = pygame.transform.scale2x(hunter)
    priest = pygame.image.load("imagens/PRIEST_Shadow.png")
    priest = pygame.transform.scale2x(priest)

    tela = pygame.display.set_mode((1024, 768))
    background = pygame.image.load("imagens/teste 3 ps.png")

    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

            tela.blit(background, (0, 0))
            tela.blit(bloco, (40, 150))
            tela.blit(paladin, (200, 300))
            tela.blit(bloco, (240, 150))
            tela.blit(rogue, (400, 300))
            tela.blit(bloco, (440, 150))
            tela.blit(wizard, (600, 300))
            tela.blit(bloco, (100, 300))
            tela.blit(hunter, (300, 600))
            tela.blit(bloco, (300, 300))
            tela.blit(priest, (500, 600))
            pygame.display.flip()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and indice > 0:
                    indice -= 1
                elif evento.key == pygame.K_RIGHT and indice < 5:
                    indice += 1
                elif evento.key == pygame.K_z:
                    if len(personagens_selecionados) < 3 and lista_personagens[indice] not in personagens_selecionados: 
                        personagens_selecionados.append(lista_personagens[indice])
                    elif len(personagens_selecionados) == 3:
                        return personagens_selecionados