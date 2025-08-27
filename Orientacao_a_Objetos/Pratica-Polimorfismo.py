class Passaro:
    def voar(self):
        print("Voando ...")

class Pardal(Passaro):
    def voar(self):
        return super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando")

#Função para chamar o método voar() dos objetos
def plano_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()
aviao = Aviao()

plano_voo(p1)
plano_voo(p2)
plano_voo(aviao)