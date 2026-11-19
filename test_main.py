#vou usar para teste sem mandar nada para o uvicorn
from fastapi.testclient import TestClient

#Estou importando aquele @app do meu main 
from main import app

cliente = TestClient(app)

#crie um teste para a minha rota /sobre
def test_root_sobre():
    resposta = cliente.get('/sobre')
    assert resposta.status_code== 200
    assert resposta.json() =={'nome': 'VAR FUTEBOL', 'versao': '1.0'}