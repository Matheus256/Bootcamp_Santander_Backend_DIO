import sqlite3 
from pathlib import Path

ROOT_PATH = Path(__file__).parent 

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

#Fazendo dessa forma evitamos que transações incompletas sejam comitadas
#Usando try, except com conexao.rollback()
try:
    cursor.execute(
        """
        INSERT INTO clientes (nome, email) VALUES (?,?);
        """,
        ('Teste1', 'teste1@gmail,com')
    )

    cursor.execute(
        """
        INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?);
        """,
        (1, 'Teste2', 'teste2@gmail,com')
    )
    conexao.commit()

except Exception as exc:
    print(f"Um erro ocorreu! {exc}")
    conexao.rollback()