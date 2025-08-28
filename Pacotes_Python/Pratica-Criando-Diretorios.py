import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__)
print(ROOT_PATH)

ROOT_PATH = Path(__file__).parent
print(ROOT_PATH)

#Criando um diretório
os.mkdir(ROOT_PATH / "Novo_Diretorio")

#Criando um arquivo no diretório criado
arquivo = open(ROOT_PATH / "Novo-Arquivo.txt", "w")
arquivo.close()

#Renomear arquivo criado
os.rename(ROOT_PATH / "Novo-Arquivo.txt", ROOT_PATH / "Arquivo-Text.txt")