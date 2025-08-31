from pydantic import BaseModel

class Categoria(BaseModel):
    nome: str

class CentroTreinamento(BaseModel):
    nome: str
    endereco: str

class Atleta(BaseModel):
    nome: str
    idade: int
    peso: float
    altura: float
    centro_treinamento_id: int
    categoria_id: int

class AtualizaAtleta(BaseModel):
    idade: int
    peso: float
    altura: float
    centro_treinamento_id: int
    categoria_id: int