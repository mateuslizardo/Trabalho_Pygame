import pygame

#Seleciona os jogadores escolhidos pelo usuário para a batalha
def selecao(lista_personagens):
    #Inicializações
    indice = 0
    personagens_selecionados = []
    seta = pygame.image.load("imagens/introcomp_seta.png")
    seta = pygame.transform.scale2x(seta)
    borda = pygame.image.load("imagens/Rectangle 2.png")
    borda_x = [160, 450, 780, 310, 620]
    borda_y = [274, 274, 274, 529, 529]

    #Desenhos
    tela = desenha_tela()
    imagem_tela = tela.copy()
    pygame.display.flip()

    #Loop principal
    executando = True
    tela.blit(seta, (30, 210))
    pygame.display.flip()
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

            if evento.type == pygame.KEYDOWN:
                #Muda a posição das setas e seleciona os personagens para a partida
                #Esquerda
                if evento.key == pygame.K_LEFT and indice > 0:
                    indice -= 1
                    x, y = pos_seta(indice)
                    tela.blit(imagem_tela, (0, 0))
                    tela.blit(seta, (x, y))
                    pygame.display.flip()
                #Direta
                elif evento.key == pygame.K_RIGHT and indice < 4:
                    indice += 1
                    x, y = pos_seta(indice)
                    tela.blit(imagem_tela, (0, 0))
                    tela.blit(seta, (x, y))
                    pygame.display.flip()
                #Seleciona
                elif evento.key == pygame.K_z:
                    if len(personagens_selecionados) < 3 and lista_personagens[indice] not in personagens_selecionados: 
                        personagens_selecionados.append(lista_personagens[indice])
                    if len(personagens_selecionados) == 3:
                        return personagens_selecionados

                #Desenha bordas
                if len(personagens_selecionados) == 1:
                    idx = lista_personagens.index(personagens_selecionados[0])
                    tela.blit(borda, (borda_x[idx], borda_y[idx]))
                    pygame.display.flip()
                if len(personagens_selecionados) == 2:
                    idx = lista_personagens.index(personagens_selecionados[0])
                    tela.blit(borda, (borda_x[idx], borda_y[idx]))
                    idx = lista_personagens.index(personagens_selecionados[1])
                    tela.blit(borda, (borda_x[idx], borda_y[idx]))
                    pygame.display.flip()

#Retorna as coordenadas da seta                    
def pos_seta(indice):
    if indice == 0:
        return 30, 210
    elif indice == 1:
        return 323, 204
    elif indice == 2:
        return 654, 204
    elif indice == 3:
        return 177, 460
    elif indice == 4:
        return 493, 460
    
#Função de Desenhos
def desenha_tela():
    fonte = pygame.font.SysFont('Inter', 32)

    #Coloca as imagens e texto no jogo
    bloco = pygame.image.load("imagens/introcomp_menu.png")
    bloco = pygame.transform.scale(bloco, (436, 436))
    introbattle_texto = pygame.image.load("imagens/introbattle.png")

    paladin = pygame.image.load("imagens/Paladino.png")
    paladin = pygame.transform.scale(paladin, (115, 115))
    paladin_texto = fonte.render('Paladin', True, (255, 255, 255))
    
    rogue = pygame.image.load("imagens/rogue.png")
    rogue = pygame.transform.scale(rogue, (115, 115))
    rogue_texto = fonte.render('Rogue', True, (255, 255, 255))
    
    wizard = pygame.image.load("imagens/wizardfinal.png")
    wizard = pygame.transform.scale(wizard, (115, 115))
    wizard_texto = fonte.render('Wizard', True, (255, 255, 255))
    
    hunter = pygame.image.load("imagens/hunter sprite.png")
    hunter = pygame.transform.scale(hunter, (115, 115))
    hunter_texto = fonte.render('Hunter', True, (255, 255, 255))
    
    priest = pygame.image.load("imagens/PRIEST_Shadow.png")
    priest = pygame.transform.scale(priest, (115, 115))
    priest_texto = fonte.render('Priest', True, (255, 255, 255))

    #Coloca a tela de fundo
    tela = pygame.display.set_mode((1024, 768))
    background = pygame.image.load("imagens/teste 3 ps.png")

    #Muda a posição das imagens
    tela.blit(background, (0, 0))
    tela.blit(bloco, (-102, 35))
    tela.blit(introbattle_texto, (380, 115))

    tela.blit(paladin, (164, 291))
    tela.blit(paladin_texto, (180, 432))

    tela.blit(bloco, (188, 35))
    tela.blit(rogue, (461, 288))
    tela.blit(rogue_texto, (475, 440))
    
    tela.blit(bloco, (512, 35))
    tela.blit(wizard, (783, 288))
    tela.blit(wizard_texto, (805, 443))

    tela.blit(bloco, (44, 291))
    tela.blit(hunter, (316, 546))
    tela.blit(hunter_texto, (330, 688))

    tela.blit(bloco, (356, 291))
    tela.blit(priest, (634, 546))
    tela.blit(priest_texto, (650, 688))

    return tela