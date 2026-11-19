#importando fast api
from fastapi import FastAPI
#importando impedimento para usar no /impedimento e a variavel fixa meio_campo
from logica_var import impedimento, MEIO_CAMPO
#para converter numeros caso necessario ou ler json ou documentar o /docs tipo um porteiro conferindo os dados
#alem disso coloquei uma virgula e importei o field ele vai me ajuda a resolver o problema da class DadosLance
from pydantic import BaseModel, Field



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
class DadosLance(BaseModel):
    atacante: float
    defensores: list[float] = Field(min_length=2)
    bola: float

#usando post em vez de get pois ele precisa receber o lance para analisar 
#usando a classe que criei DadosLance usei ela como parametro e passei a variavel e o tipo 
@app.post('/impedimento')
async def root_impedimento(lance: DadosLance):
#aqui dei um return da decisao baseado no dados do lance que vai ser passado na class dados lance
    return{'decisao': impedimento(lance.atacante, lance.defensores, lance.bola, MEIO_CAMPO)}

