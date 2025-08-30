import sqlite3 
from pathlib import Path

ROOT_PATH = Path(__file__).parent 

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()

def criar_tabela(conexao, cursor):
    cursor.execute(
        """
        CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100), email VARCHAR(150));
        """
    )
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?);', data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute(
        """
        UPDATE clientes SET nome = ?, email = ? WHERE id = ?;
        """,
        data
    )
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id, )
    cursor.execute(
        """
        DELETE FROM clientes WHERE id = ?;
        """,
        data
    )
    conexao.commit()

def recuperar_registro(cursor, id):
    cursor.execute(
        """
        SELECT * FROM clientes WHERE id = ?;
        """,
        (id, )
    )
    resultado = cursor.fetchone()
    return resultado

def todos_registros(cursor, order = False):
    if order:
        return cursor.execute("SELECT * FROM clientes ORDER BY nome;")
    
    return cursor.execute("SELECT * FROM clientes;")

atualizar_registro(conexao, cursor, "Matheus", "matheus@gmail.com", 1)
inserir_registro(conexao, cursor, "Isabella", "bella@gmail.com")
inserir_registro(conexao, cursor, "Batman", "bat@gmail.com")
excluir_registro(conexao, cursor, 4)

cliente = recuperar_registro(cursor, 2)
print(cliente)

print("")

clientes = todos_registros(cursor)
for cliente in clientes:
    print(cliente)

print("")

clientes = todos_registros(cursor, order = True)
for cliente in clientes:
    print(cliente)