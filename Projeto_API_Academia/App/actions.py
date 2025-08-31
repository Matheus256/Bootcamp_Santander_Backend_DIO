from pathlib import Path
import sqlite3

from models import Atleta, CentroTreinamento, Categoria, AtualizaAtleta

ROOT_PATH = Path(__file__).parent.parent

DATABASE_URI = ROOT_PATH / "Workout.db"
_connection: sqlite3.Connection

def cadastro_centro_treinamento(centro: CentroTreinamento, cursor: sqlite3.Cursor) -> str:
    try:
        query = "INSERT INTO CentroTreinamento(nome, endereco) VALUES (?,?);"
        values = (centro.nome, centro.endereco)
        cursor.execute(query, values)
        _connection.commit()
        status = "Centro de treinamento cadastrado com sucesso!"
    except:
        status = "Erro ao cadastrar o centro de treinamento"
        _connection.rollback()
    
    return status

def cadastro_categoria(categoria: Categoria, cursor: sqlite3.Cursor) -> str:
    try:
        query = "INSERT INTO Categoria(nome) VALUES (?);"
        values = (categoria.nome, )
        cursor.execute(query, values)
        _connection.commit()
        status = "Categoria cadastrada com sucesso."
    except:
        status = "Erro ao cadastra a categoria."
        _connection.rollback()

    return status

def centros_treinamentos(cursor: sqlite3.Cursor):
    cursor.execute("SELECT * FROM CentroTreinamento;")
    return cursor.fetchall()

def consulta_atletas(cursor: sqlite3.Cursor):
    cursor.execute(
        """
        SELECT
        a.nome "Nome",
        a.idade "Idade",
        a.peso "Peso",
        a.altura "Altura",
        ce.nome "Centro de Treinamento",
        ca.nome "Categoria"
        FROM Atletas a
        JOIN CentroTreinamento ce ON a.centro_treinamento_id = ce.id
        JOIN Categoria ca ON a.categoria_id = ca.id;
        """
    )
    return cursor.fetchall()

def consulta_atleta(cursor: sqlite3.Cursor, id: int):
    cursor.execute(
        """
        SELECT
        a.nome "Nome",
        a.idade "Idade",
        a.peso "Peso",
        a.altura "Altura",
        ce.nome "Centro de Treinamento",
        ca.nome "Categoria"
        FROM Atletas a
        JOIN CentroTreinamento ce ON a.centro_treinamento_id = ce.id
        JOIN Categoria ca ON a.categoria_id = ca.id
        WHERE a.id = (?)
        """,
        (id,)
    )
    return cursor.fetchone()


def consulta_categorias(cursor: sqlite3.Cursor):
    cursor.execute("SELECT * FROM Categoria;")
    return cursor.fetchall()

def cadastro_atleta(atleta: Atleta, cursor: sqlite3.Cursor) -> str:
    try:
        query = "INSERT INTO Atletas(nome, idade, peso, altura, centro_treinamento_id, categoria_id) VALUES (?,?,?,?,?,?);"
        values = (
            atleta.nome,
            atleta.idade,
            atleta.peso,
            atleta.altura,
            atleta.centro_treinamento_id,
            atleta.categoria_id
        )
        cursor.execute(query, values)
        _connection.commit()
        status = "Atleta cadastrado com sucesso!"
    except:
        status = "Erro ao cadastrar atleta."
        _connection.rollback()
    
    return status

def remove_atleta(cursor: sqlite3.Cursor, id: int) -> str:
    try:
        cursor.execute(
            "DELETE FROM Atletas WHERE id = (?);", (id,)
        )
        _connection.commit()
        status = "Atleta removido com sucesso!"
    except:
        status = "Erro ao remover atleta"
        _connection.rollback()
    
    return status

def atualiza_atleta(cursor: sqlite3.Cursor, atleta: AtualizaAtleta, atleta_id: int):
    try:
        cursor.execute(
            """
            UPDATE Atletas
            SET idade = ?,
            peso = ?,
            altura = ?,
            centro_treinamento_id = ?,
            categoria_id = ?
            WHERE id = ?;
            """,
            (atleta.idade, atleta.peso, atleta.altura, atleta.centro_treinamento_id, atleta.categoria_id, atleta_id)
        )
        _connection.commit()
        status = "Dados do atleta atualizados."
    except:
        status = "Erro ao atualizar os dados do atleta."
        _connection.rollback()
    
    return status


def get_sql_cursor() -> sqlite3.Cursor:
    global _connection
    _connection = sqlite3.connect(database = DATABASE_URI, check_same_thread = False)
    return _connection.cursor()

def init_base(cursor: sqlite3.Cursor) -> None:
    #Criação da Tabela para as categorias de treinos
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Categoria (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS CentroTreinamento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(200) NOT NULL,
        endereco VAR(200) NOT NULL
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Atletas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        peso DECIMAL(5,2) NOT NULL,
        altura DECIMAL(5,2) NOT NULL,
        centro_treinamento_id INT,
        categoria_id INT,
        FOREIGN KEY (centro_treinamento_id) REFERENCES CentroTreinamento(id), 
        FOREIGN KEY (categoria_id) REFERENCES Categoria(id)
        );
        """
    )
    