class Personagem:
    def __init__(self, vida, ataque, defesa, velocidade, nome, imagem, vida_inicial):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.nome = nome
        self.imagem = imagem
        self.vida_inicial = vida_inicial

    def __str__(self): 
        return f"{self.nome}"
    
    def __repr__(self):
        return f"{self.nome}"

    #Ordena as listas com base na velocidade
    def maior_velocidade(lista_personagens):
        return lista_personagens.sort(key=lambda personagem: personagem.velocidade, reverse=True)
    
    #Retorna o dano causado pelas ações
    def gera_dano(atacante, atacado):
        dano = int((atacante.ataque)*(50/(50+atacado.defesa)))
        return dano
    
    #Diminui a quantidade de dano que o personagem receberá na próxima partida
    def acao_defesa(personagem):
        return personagem.defesa * 2
    
    #retorna se o personagem morreu
    def verifica_morte(personagem):
        if personagem.vida <= 0:
            return True
        else:
            return False
        
    #retorna o link da imagem
    def link_imagem(personagem):
        return f"{personagem.imagem}"