import pygame
def selecao(lista_personagens):
    indice = 0
    personagens_selecionados = []
    for evento in pygame.event.get():
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