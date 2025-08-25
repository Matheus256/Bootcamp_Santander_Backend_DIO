class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim Plim")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parou")

    def correr(self):
        print("Vrummmmm...")

    #Sobrecarga para usar com print
    #def __str__(self):
    #    return f"Bicicleta -> cor: {self.cor}, modelo: {self.modelo}, ano: {self.ano}, valor: {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

bicicleta1 = Bicicleta("Vermelha", "caloi", 2022, 600)

bicicleta1.buzinar()
bicicleta1.correr()
bicicleta1.parar()

print(f"Informações da bicleta1 -> cor: {bicicleta1.cor}, modelo: {bicicleta1.modelo}, ano: {bicicleta1.ano}, valor: {bicicleta1.valor} ")
print("")
print(bicicleta1)