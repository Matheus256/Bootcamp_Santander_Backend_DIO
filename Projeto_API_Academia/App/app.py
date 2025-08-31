from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from typing import Union 

from actions import *
from models import Atleta, CentroTreinamento, Categoria, AtualizaAtleta

app = FastAPI()
cursor: sqlite3.Cursor

@app.on_event("startup")
def init_database():
    global cursor
    cursor = get_sql_cursor()
    init_base(cursor = cursor)

@app.post("/cadastro-atleta")
def cadastrar_atleta(atleta: Atleta) -> str:
    resp = cadastro_atleta(atleta = atleta, cursor = cursor)
    return resp

@app.post("/cadastro-centro-treinamento")
def cadastrar_centro_treinamento(centro: CentroTreinamento) -> str:
    resp = cadastro_centro_treinamento(centro = centro, cursor = cursor)
    return resp

@app.post("/cadastro-categoria")
def cadastrar_categoria(categoria: Categoria) -> str:
    resp = cadastro_categoria(categoria = categoria, cursor = cursor)
    return resp

@app.get("/centros")
def retorna_centros_treinamento():
    centros = centros_treinamentos(cursor = cursor)
    return centros

@app.get("/atletas")
def retorna_atletas():
    atletas = consulta_atletas(cursor = cursor)
    return atletas

@app.get("/atleta")
def retorna_atleta(id: int):
    resp = consulta_atleta(cursor = cursor, id = id)
    return resp

@app.get("/categorias")
def retorna_categorias():
    categorias = consulta_categorias(cursor = cursor)
    return categorias

@app.delete("/remover-atleta")
def remover_atleta(id: int):
    resp = remove_atleta(cursor = cursor, id = id)
    return resp

@app.put("/atualizar-atleta/{atleta_id}")
def atualizar_atleta(atleta_id: int, atleta: AtualizaAtleta):
    resp = atualiza_atleta(cursor = cursor, atleta = atleta, atleta_id = atleta_id)
    return resp

if __name__ == "__main__":
    uvicorn.run(app, port = 8000)