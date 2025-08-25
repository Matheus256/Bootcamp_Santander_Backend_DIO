from abc import ABC, abstractmethod, abstractproperty

#ABC obriga a sobrescrita
class ControleRemoto(ABC):
    @abstractmethod 
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV...")
        print("Ligado")

    def desligar(self):
        print("Desligando TV...")
        print("Desligado")

    @property
    def marca(self):
        return "Sansung"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando Ar Condicionado...")
        print("Ligado")

    def desligar(self):
        print("Desligando Ar Condicionado...")
        print("Desligado")
    
    @property
    def marca(self):
        return "LG"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)
print("")

con = ControleArCondicionado()
con.ligar()
con.desligar()