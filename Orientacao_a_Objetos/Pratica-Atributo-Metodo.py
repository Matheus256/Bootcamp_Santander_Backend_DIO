class Estudante:
    #Atributo da classe -> Todas as instâncias tem o mesmo valor
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"


#Automatizando o print dos atributos
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

estu1 = Estudante("Matheus", 14)
estu2 = Estudante("Isabella", 7)

mostrar_valores(estu1, estu2)

#Muda em todas as instâncias
Estudante.escola = "Euclides"

#estu1.escola = "Pitagoras" #Altera apenas nesta instância

mostrar_valores(estu1, estu2)