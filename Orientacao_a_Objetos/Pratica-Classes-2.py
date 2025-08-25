class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print(f"Inicializando a instância de {nome}...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print(f"Removendo a instância de {self.nome}")

    def falar(self):
        print("Au au!")

cachorro = Cachorro("Stitch", "azul")
cachorro.falar()
cachorro.falar()