#importando fast api
from fastapi import FastAPI

#criando um obj dele 
app = FastAPI()

#o @ seria tipo um etiqueta por enquanto apos entender mais
#get o tipo de pedido 
#'/' seria um se for isso '/impedimento' o impedimento seria o localhost:8000/impedimento
@app.get('/')

#criar funcao root
#async pesquisar no futuro por enquanto ignore 
#retorna 
async def root():
    return{"status": "VAR online"}

#aqui estou criando uma rota para explicar oque faz tipo nome: var e versao que esta na 1.0
@app.get('/sobre')
async def root_sobre():
    return{'nome': 'VAR FUTEBOL',
           'versao': '1.0'}