#vou usar para teste sem mandar nada para o uvicorn
from fastapi.testclient import TestClient

from logica_var import impedimento, MEIO_CAMPO


#Estou importando aquele @app do meu main 
from main import app

cliente = TestClient(app)

#crie um teste para a minha rota /sobre
def test_root_sobre():
    resposta = cliente.get('/sobre')
    assert resposta.status_code== 200
    assert resposta.json() =={'nome': 'VAR FUTEBOL', 'versao': '1.0'}

#teste para a rota do impedimento caso esteja impedido
def test_root_impedimento():
    resposta = cliente.post('/impedimento', json = {'atacante':80, 'defensores' : [75, 100, 78.5, 60], 'bola': 60})
    assert resposta.status_code == 200
    assert resposta.json() == {'decisao': 'jogador impedido'}

#teste para a rota do impedimento caso esteja nao esteja impedido
def test_root_nao_impedimento():
    resposta = cliente.post('/impedimento', json = {'atacante':77, 'defensores' : [75, 100, 78.5, 60], 'bola': 60})
    assert resposta.status_code == 200
    assert resposta.json() == {'decisao': 'jogador nao esta impedido'}

#teste para a rota impedimento caso tenha apenas um defensor
def test_root_um_defensor():
    resposta = cliente.post('/impedimento', json = {'atacante':77, 'defensores' : [75], 'bola': 60})
    assert resposta.status_code == 422

