class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado = False):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Não"} estou carregado")

moto = Motocicleta("vermelha", "abc-1234",2)
print(moto)
moto.ligar_motor()

carro = Carro("preto", "xde-0098",4)
carro.ligar_motor()

caminhao = Caminhao("branco", "gfd-8712",8)
caminhao.ligar_motor()
caminhao.esta_carregado()
print("")
print(moto)
print(carro)
print(caminhao)