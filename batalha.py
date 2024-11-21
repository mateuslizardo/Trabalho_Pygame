import pygame
from personagem import *

ataque = 1
defesa = 2
necromante = 3
esqueleto = 4
necromancer = Personagem(180, 35, 25, 15, "necromancer", "", 180)
skeleton = Personagem(150, 25, 20, 10, "skeleton", "", 150)


def batalha(herois):
    global inimigos
    inimigos = [necromancer, skeleton]
    cont = 0
    modo_escolhido = 0
    escolheu_defender = False
    clock = pygame.time.Clock()
    clock.tick(120)

    maior_velocidade(herois)
    tela = desenha_batalha(herois)
    escrever_turno(herois, cont, tela)
    vida_personagens(herois, tela)
    pos_seta = ataque
    desenha_seta(pos_seta, tela)
    pygame.display.flip()
    
    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

            if evento.type == pygame.KEYDOWN:
                if not(cont == 1 or cont == 3 or cont == 5):
                    if evento.key == pygame.K_RIGHT and pos_seta == ataque:
                        pos_seta = defesa
                        bloco_maior = pygame.image.load("imagens/bloco_maior.png")
                        tela.blit(bloco_maior, (59, 492))
                        escrever_turno(herois, cont, tela)
                        desenha_seta(pos_seta, tela)
                        pygame.display.flip()

                    elif evento.key == pygame.K_LEFT and pos_seta == defesa:
                        pos_seta = ataque
                        bloco_maior = pygame.image.load("imagens/bloco_maior.png")
                        tela.blit(bloco_maior, (59, 492))
                        desenha_seta(pos_seta, tela)  
                        escrever_turno(herois, cont, tela)
                        pygame.display.flip()

                    elif evento.key == pygame.K_z and modo_escolhido == 0:
                        modo_escolhido = pos_seta
                        if pos_seta == ataque:
                            pos_seta = necromante
                            bloco_maior = pygame.image.load("imagens/bloco_maior.png")
                            tela.blit(bloco_maior, (59, 492))
                            desenha_seta(pos_seta, tela)  
                            escrever_turno(herois, cont, tela)
                            pygame.display.flip()
                            continue
                    
                    if modo_escolhido == ataque:
                        if evento.key == pygame.K_x:
                            modo_escolhido = 0
                            pos_seta = ataque
                            desenha_batalha(herois)
                            desenha_seta(pos_seta, tela)  
                            escrever_turno(herois, cont, tela)
                            vida_personagens(herois, tela)
                            pygame.display.flip()
                            
                        elif evento.key == pygame.K_DOWN and pos_seta == necromante:
                            pos_seta = esqueleto
                            desenha_batalha(herois)
                            desenha_seta(pos_seta, tela)  
                            escrever_turno(herois, cont, tela)
                            vida_personagens(herois, tela)
                            pygame.display.flip()

                        elif evento.key == pygame.K_UP and pos_seta == esqueleto:
                            pos_seta = necromante
                            desenha_batalha(herois)
                            desenha_seta(pos_seta, tela)  
                            escrever_turno(herois, cont, tela)
                            vida_personagens(herois, tela)
                            pygame.display.flip()

                        elif evento.key == pygame.K_z:
                            dano = herois[cont//2].gera_dano(inimigos[pos_seta - 3])
                            inimigos[pos_seta - 3].vida -= dano
                            print(inimigos[pos_seta - 3].vida, pos_seta)

                            if cont < 5:
                                cont += 1
                            elif cont == 5:
                                cont = 0

                            modo_escolhido = 0
                            pos_seta = ataque
                            desenha_batalha(herois)
                            escrever_turno(herois, cont, tela)
                            vida_personagens(herois, tela)
                            pygame.display.flip()

                    elif modo_escolhido == defesa:
                        herois[cont//2].defesa = herois[cont//2].acao_defesa()
                        escolheu_defender = True
                        if cont < 5:
                            cont += 1
                        elif cont == 5:
                            cont = 0

                        modo_escolhido = 0
                        pos_seta = ataque
                        bloco_maior = pygame.image.load("imagens/bloco_maior.png")
                        tela.blit(bloco_maior, (59, 492))
                        escrever_turno(herois, cont, tela)
                        pygame.display.flip()

                elif cont == 1:
                    dano = inimigos[0].gera_dano(herois[0])
                    herois[0].vida -= dano
                    if escolheu_defender == True:
                        herois[0].defesa /= 2
                        escolheu_defender = False

                    if cont < 5:
                        cont += 1
                    elif cont == 5:
                        cont = 0

                    bloco_maior = pygame.image.load("imagens/bloco_maior.png")
                    bloco_menor = pygame.image.load("imagens/bloco_menor.png")
                    tela.blit(bloco_maior, (59, 492))
                    tela.blit(bloco_menor, (604, 492))
                    escrever_turno(herois, cont, tela)
                    vida_personagens(herois, tela)
                    desenha_seta(pos_seta, tela)
                    pygame.display.flip()

                elif cont == 3:
                    dano = inimigos[1].gera_dano(herois[1])
                    herois[1].vida -= dano
                    if escolheu_defender == True:
                        herois[1].defesa /= 2
                        escolheu_defender = False

                    if cont < 5:
                        cont += 1
                    elif cont == 5:
                        cont = 0

                    bloco_maior = pygame.image.load("imagens/bloco_maior.png")
                    bloco_menor = pygame.image.load("imagens/bloco_menor.png")
                    tela.blit(bloco_maior, (59, 492))
                    tela.blit(bloco_menor, (604, 492))
                    escrever_turno(herois, cont, tela)
                    vida_personagens(herois, tela)
                    desenha_seta(pos_seta, tela)
                    pygame.display.flip()

                elif cont == 5:
                    dano = inimigos[1].gera_dano(herois[2])
                    herois[2].vida -= dano
                    if escolheu_defender == True:
                        herois[2].defesa /= 2
                        escolheu_defender = False

                    if cont < 5:
                        cont += 1
                    elif cont == 5:
                        cont = 0

                    bloco_maior = pygame.image.load("imagens/bloco_maior.png")
                    bloco_menor = pygame.image.load("imagens/bloco_menor.png")
                    tela.blit(bloco_maior, (59, 492))
                    tela.blit(bloco_menor, (604, 492))
                    escrever_turno(herois, cont, tela)
                    vida_personagens(herois, tela)
                    desenha_seta(pos_seta, tela)
                    pygame.display.flip()

            herois, inimigos = alguem_morreu(herois, inimigos)
            if len(herois) == 0 or len(inimigos) == 0:
                executando = False

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

    elif cont == 3 or cont == 5:
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

def desenha_seta(pos_seta, tela):
    if pos_seta == ataque:
        seta = pygame.image.load("imagens/introcomp_seta.png")
        seta = pygame.transform.scale(seta, (256, 256))
        seta = pygame.transform.rotate(seta, 90)
        tela.blit(seta, (42, 525))
        
    elif pos_seta == defesa:
        seta = pygame.image.load("imagens/introcomp_seta.png")
        seta = pygame.transform.scale(seta, (256, 256))
        seta = pygame.transform.rotate(seta, 90)
        tela.blit(seta, (352, 525))

    elif pos_seta == necromante:
        seta = pygame.image.load("imagens/introcomp_seta.png")
        seta = pygame.transform.scale(seta, (256, 256))
        seta = pygame.transform.rotate(seta, 90)
        tela.blit(seta, (674, 170))

    elif pos_seta == esqueleto:
        seta = pygame.image.load("imagens/introcomp_seta.png")
        seta = pygame.transform.scale(seta, (256, 256))
        seta = pygame.transform.rotate(seta, 90)
        tela.blit(seta, (639, 340))

def alguem_morreu(herois, inimigos):
    for i in len(herois):
        if herois[i].verifica_morte() == True:
            herois[i].pop(i)

    for i in len(inimigos):
        if inimigos[i].verifica_morte() == True:
            inimigos[i].pop(i)

    return herois, inimigos