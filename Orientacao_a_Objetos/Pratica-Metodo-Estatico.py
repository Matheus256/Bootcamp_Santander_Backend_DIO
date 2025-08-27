class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(self, ano, mes, dia, nome):
        idade = 2025 - ano
        return Pessoa(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

#p = Pessoa("Matheus", 27)
#print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_data_nascimento(1998, 2, 19, "Matheus")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(27))