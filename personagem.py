class Personagem:
    def __init__(self, vida, ataque, defesa, velocidade, nome, imagem):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.nome = nome
        self.imagem = imagem

    def __str__(self): 
        return f"{self.nome}"
    
    def __repr__(self):
        return f"{self.nome}"

    def maior_velocidade(lista_personagens):
        mais_rapido = lista_personagens[0] 
        for personagem in lista_personagens: 
            if personagem.velocidade > mais_rapido.velocidade: 
                mais_rapido = personagem 
        return mais_rapido
    
    def gera_dano(atacante, atacado):
        dano = (atacante.ataque)*(50/(50+atacado.defesa))
        return dano
    
    def acao_defesa(personagem):
        return personagem.defesa * 2
    
    def verifica_morte(personagem):
        if personagem.vida <= 0:
            return True
        else:
            return False
        
    def link_imagem(personagem):
        return f"{personagem.imagem}"