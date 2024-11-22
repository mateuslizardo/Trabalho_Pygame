from personagem import *
import pygame
import tela_inicial
import batalha
import tela_final

#Personagens
paladin = Personagem(250, 20, 40, 15, "paladin", "imagens/Paladino.png", 250)
rogue = Personagem(120, 30, 20, 30, "rogue", "imagens/rogue.png", 120)
wizard = Personagem(100, 40, 10, 25, "wizard", "imagens/wizardfinal 2.png", 100)
hunter = Personagem(180, 25, 30, 20, "hunter", "imagens/hunter sprite.png", 180)
priest = Personagem(150, 10, 35, 10, "priest", "imagens/PRIEST_Shadow.png", 150)

lista_personagens = [paladin, rogue, wizard, hunter, priest]

#Inicializações
pygame.init()
pygame.font.init()

#Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    #Seleciona os jogadores escolhidos pelo usuário para a batalha   
    herois = tela_inicial.selecao(lista_personagens)
    herois_copia = herois.copy()
    #Realiza a lógica da batalha
    venceu = batalha.batalha(herois)
    tela_final.resultado(herois_copia, venceu)
    executando = False