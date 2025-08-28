import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / 'usuarios.csv', 'w', encoding = 'utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Isabella'])
        escritor.writerow(['2', 'Matheus'])        
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")
