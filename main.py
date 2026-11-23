#importando fast api
from fastapi import FastAPI
#importando impedimento para usar no /impedimento e a variavel fixa meio_campo
from logica_var import impedimento, MEIO_CAMPO
#para converter numeros caso necessario ou ler json ou documentar o /docs tipo um porteiro conferindo os dados
#alem disso coloquei uma virgula e importei o field ele vai me ajuda a resolver o problema da class DadosLance
from pydantic import BaseModel, Field
#importar o date para dadosLance
from datetime import date
#usando para importar o lance e o motor
from database import Lance, engine
#importando a Session
from sqlmodel import Session
#importando o json
import json

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

#usei o Field pois quando minha lista vier com menos jogadores e apenas 1 sera o goleiro entao nao tem pq impedir
#vou usar field para limitar o tempo e minuto e segundo usando tipo uma regra de >= <= ou == e etc 
#gt maior que| ge maior ou igual |lt menor que | le maior ou igual 
#coloquei um max_length e min_lenght pois se tiver 1 defensor sera o goleiro e max pois so pode ter 11 jogadores em campo
class DadosLance(BaseModel):
    jogo : str
    data : date
    tempo : int = Field (ge = 1, le= 4)
    minuto : int = Field (ge=0,le=130)
    segundo : int = Field (ge=0,le=59)
    time : str
    jogador : str
    atacante: float
    defensores: list[float] = Field(min_length=2, max_length=11)
    bola: float

#usando post em vez de get pois ele precisa receber o lance para analisar 
#usando a classe que criei DadosLance usei ela como parametro e passei a variavel e o tipo 
#criei uma variavel decisao para o return passar apenas o decisao
#criei o salvar lance para depois salvar dentro do meu banco de dados
@app.post('/impedimento')
async def root_impedimento(lance: DadosLance):
#aqui dei um return da decisao baseado no dados do lance que vai ser passado na class dados lance
    decisao = impedimento(lance.atacante, lance.defensores, lance.bola, MEIO_CAMPO)
    salvar_lance = Lance(jogo=lance.jogo, data=lance.data,tempo=lance.tempo,minuto=lance.minuto,segundo=lance.segundo,time=lance.time,jogador=lance.jogador,
    atacante=lance.atacante,defensores=json.dumps(lance.defensores), bola=lance.bola,decisao = decisao
    )
    return{'decisao': decisao}

