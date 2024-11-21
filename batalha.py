import pygame
from personagem import *

ataque = 1
defesa = 2
necromante = 3
esqueleto = 4
necromancer = Personagem(180, 35, 25, 15, "necromancer", "imagens/Sprite-0001 1.png", 180)
skeleton = Personagem(150, 25, 20, 10, "skeleton", "imagens/caveira sprite 2 1.png", 150)


def batalha(herois):
    inimigos = [necromancer, skeleton]
    cont_herois = 0
    cont_inimigos = 0
    modo_escolhido = 0
    escolheu_defender = False
    vez_heroi = True
    vez_vilao = False
    clock = pygame.time.Clock()
    clock.tick(120)

    maior_velocidade(herois)
    tela = pygame.display.set_mode((1024, 768))
    desenha_batalha(herois, tela, inimigos)
    escrever_turno(herois[cont_herois], tela, vez_heroi)
    vida_personagens(herois, tela)
    pos_seta = ataque
    desenha_seta(pos_seta, tela)
    pygame.display.flip()
    
    executando = True
    while executando:
        for evento in pygame.event.get():
            print(cont_inimigos, len(inimigos)-1, len(herois)-1)
            if evento.type == pygame.QUIT:
                executando = False

            if evento.type == pygame.KEYDOWN:
                if vez_heroi == True:
                    if evento.key == pygame.K_RIGHT and pos_seta == ataque:
                        pos_seta = defesa
                        bloco_maior = pygame.image.load("imagens/bloco_maior.png")
                        tela.blit(bloco_maior, (59, 492))
                        escrever_turno(herois[cont_herois], tela, vez_heroi)
                        desenha_seta(pos_seta, tela)
                        pygame.display.flip()

                    elif evento.key == pygame.K_LEFT and pos_seta == defesa:
                        pos_seta = ataque
                        bloco_maior = pygame.image.load("imagens/bloco_maior.png")
                        tela.blit(bloco_maior, (59, 492))
                        desenha_seta(pos_seta, tela)  
                        escrever_turno(herois[cont_herois], tela, vez_heroi)
                        pygame.display.flip()

                    elif evento.key == pygame.K_z and modo_escolhido == 0:
                        modo_escolhido = pos_seta
                        if pos_seta == ataque:
                            pos_seta = necromante
                            bloco_maior = pygame.image.load("imagens/bloco_maior.png")
                            tela.blit(bloco_maior, (59, 492))
                            desenha_seta(pos_seta, tela)  
                            escrever_turno(herois[cont_herois], tela, vez_heroi)
                            pygame.display.flip()
                            continue
                    
                    if modo_escolhido == ataque:
                        if evento.key == pygame.K_x:
                            modo_escolhido = 0
                            pos_seta = ataque
                            desenha_batalha(herois, tela, inimigos)
                            desenha_seta(pos_seta, tela)  
                            escrever_turno(herois[cont_herois], tela, vez_heroi)
                            vida_personagens(herois, tela)
                            pygame.display.flip()
                            
                        elif evento.key == pygame.K_DOWN and pos_seta == necromante and len(inimigos) == 2:
                            pos_seta = esqueleto
                            desenha_batalha(herois, tela, inimigos)
                            desenha_seta(pos_seta, tela)  
                            escrever_turno(herois[cont_herois], tela, vez_heroi)
                            vida_personagens(herois, tela)
                            pygame.display.flip()

                        elif evento.key == pygame.K_UP and pos_seta == esqueleto:
                            pos_seta = necromante
                            desenha_batalha(herois, tela, inimigos)
                            desenha_seta(pos_seta, tela)  
                            escrever_turno(herois[cont_herois], tela, vez_heroi)
                            vida_personagens(herois, tela)
                            pygame.display.flip()

                        elif evento.key == pygame.K_z:
                            dano = herois[cont_herois].gera_dano(inimigos[pos_seta - 3])
                            inimigos[pos_seta - 3].vida -= dano

                            herois, inimigos = alguem_morreu(herois, inimigos)
                            if cont_inimigos >= len(inimigos):
                                cont_inimigos = 0
                            if len(inimigos) == 0:
                                return True
                            elif len(herois) == 0:
                                return False
            
                            print(inimigos[pos_seta - 3].vida, pos_seta)

                            if cont_herois < len(herois)-1:
                                cont_herois += 1
                            elif cont_herois >= len(herois)-1:
                                cont_herois = 0

                            modo_escolhido = 0
                            vez_heroi = False
                            vez_vilao = True
                            pos_seta = ataque
                            desenha_batalha(herois, tela, inimigos)
                            escrever_turno(inimigos[cont_inimigos], tela, vez_heroi)
                            vida_personagens(herois, tela)
                            pygame.display.flip()

                    elif modo_escolhido == defesa:
                        herois[cont_herois].defesa = herois[cont_herois].acao_defesa()
                        escolheu_defender = True

                        if cont_herois < len(herois)-1:
                            cont_herois += 1
                        elif cont_herois >= len(herois)-1:
                            cont_herois = 0

                        modo_escolhido = 0
                        vez_heroi = False
                        vez_vilao = True
                        pos_seta = ataque
                        bloco_maior = pygame.image.load("imagens/bloco_maior.png")
                        tela.blit(bloco_maior, (59, 492))
                        escrever_turno(inimigos[cont_inimigos], tela, vez_heroi)
                        pygame.display.flip()

                elif vez_vilao == True:
                    dano = inimigos[cont_inimigos].gera_dano(herois[cont_herois - 1])
                    herois[cont_herois - 1].vida -= dano

                    herois, inimigos = alguem_morreu(herois, inimigos)
                    if cont_herois >= len(herois):
                        cont_herois = 0
                    if len(inimigos) == 0:
                        return True
                    elif len(herois) == 0:
                        return False

                    if escolheu_defender == True:
                        herois[cont_herois - 1].defesa /= 2
                        escolheu_defender = False

                    if cont_inimigos < len(inimigos)-1:
                        cont_inimigos += 1
                    elif cont_inimigos >= len(inimigos)-1:
                        cont_inimigos = 0

                    vez_heroi = True
                    vez_vilao = False

                    bloco_maior = pygame.image.load("imagens/bloco_maior.png")
                    bloco_menor = pygame.image.load("imagens/bloco_menor.png")
                    tela.blit(bloco_maior, (59, 492))
                    tela.blit(bloco_menor, (604, 492))
                    desenha_batalha(herois, tela, inimigos)
                    escrever_turno(herois[cont_herois], tela, vez_heroi)
                    vida_personagens(herois, tela)
                    desenha_seta(pos_seta, tela)
                    pygame.display.flip()

            if cont_herois > len(herois)-1:
                cont_herois = 0
            if cont_inimigos > len(inimigos)-1:
                cont_inimigos = 0

            herois, inimigos = alguem_morreu(herois, inimigos)
            if len(inimigos) == 0:
                return True
            elif len(herois) == 0:
                return False

def maior_velocidade(lista_personagens):
        return lista_personagens.sort(key=lambda personagem: personagem.velocidade, reverse=True)

def desenha_batalha(herois, tela, inimigos):
    background = pygame.image.load("imagens/Batalha 2.png")
    tela.blit(background, (0, 0))
    
    if len(herois) >= 1:
        heroi0 = pygame.image.load(herois[0].imagem)
        heroi0 = pygame.transform.scale(heroi0, (124, 124))
        tela.blit(heroi0, (221, 160))

    if len(herois) >= 2:
        heroi1 = pygame.image.load(herois[1].imagem)
        heroi1 = pygame.transform.scale(heroi1, (124, 124))
        tela.blit(heroi1, (110, 269))

    if len(herois) >= 3:
        heroi2 = pygame.image.load(herois[2].imagem)
        heroi2 = pygame.transform.scale(heroi2, (124, 124))
        tela.blit(heroi2, (221, 360))

    if len(inimigos) >= 1:
        inimigo0 = pygame.image.load(inimigos[0].imagem)
        tela.blit(inimigo0, (864, 171))

    if len(inimigos) >= 2:
        inimigo1 = pygame.image.load(inimigos[1].imagem)
        tela.blit(inimigo1, (802, 334))

    return tela

def escrever_turno(personagem, tela, vez_heroi):
    fonte = pygame.font.SysFont('Inter', 48)

    if vez_heroi == True:
        texto = fonte.render(f"{personagem}'s turn!", True, (255, 255, 255))
        tela.blit(texto, (112, 518))
        texto = fonte.render("attack", True, (255, 255, 255))
        tela.blit(texto, (112, 575))
        texto = fonte.render("defend", True, (255, 255, 255))
        tela.blit(texto, (420, 575))
        texto = fonte.render("insight", True, (255, 255, 255))
        tela.blit(texto, (112, 632))
        texto = fonte.render("skill", True, (255, 255, 255))
        tela.blit(texto, (420, 632))

    else:
        texto = fonte.render(f"{personagem}'s turn!", True, (255, 255, 255))
        tela.blit(texto, (112, 518))

def vida_personagens(herois, tela):
    fonte = pygame.font.SysFont('Inter', 48)

    if len(herois) >= 1:
        texto = fonte.render(f"{herois[0]}", True, (255, 255, 255))
        tela.blit(texto, (630, 518))
        texto = fonte.render(f"{herois[0].vida} / {herois[0].vida_inicial}", True, (255, 255, 255))
        tela.blit(texto, (788, 518))

    if len(herois) >= 2:
        texto = fonte.render(f"{herois[1]}", True, (255, 255, 255))
        tela.blit(texto, (630, 575))
        texto = fonte.render(f"{herois[1].vida} / {herois[1].vida_inicial}", True, (255, 255, 255))
        tela.blit(texto, (788, 578))

    if len(herois) >= 3:
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
    for heroi in herois[:]:
        if heroi.verifica_morte():
            herois.remove(heroi)

    for inimigo in inimigos[:]:
        if inimigo.verifica_morte():
            inimigos.remove(inimigo)

    return herois, inimigos