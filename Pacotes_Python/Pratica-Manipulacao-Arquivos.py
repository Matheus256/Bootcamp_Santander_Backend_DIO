arquivo = open("./lorem.txt", "r")
print(arquivo.read())
arquivo.close()

#Usando o readlines
arquivo = open("./lorem.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

#Outra forma com readline
arquivo = open("./lorem.txt", "r")
while len(linha := arquivo.readline()):
    print(linha)
arquivo.close()

#Agora fazendo uma alteração no arquivo
arquivo = open("./teste.txt", "w")
arquivo.write("Olá Mundo!")
arquivo.close()

#Escrevendo linhas no arquivo
arquivo = open("./teste.txt", "w")
arquivo.writelines(["\nNova linha", "\nÚltima linha"])
arquivo.close()

#Melhor forma de abrir um arquivo
with open("./lorem.txt", "r") as arquivo:
    print(arquivo.read())
