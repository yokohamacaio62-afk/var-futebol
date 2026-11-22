#vou usar para teste sem mandar nada para o uvicorn
from fastapi.testclient import TestClient

from logica_var import impedimento, MEIO_CAMPO


#Estou importando aquele @app do meu main 
from main import app

cliente = TestClient(app)

#criei esses LANCE_VALIDO para nao ficar repetindo o codigo e apenas colocar copy
LANCE_VALIDO = {
        'jogo' : 'Corinthians x Palmeiras',
        'data': '2026-03-17',
        'tempo': 1,
        'minuto': 34,
        'segundo': 12,
        'time': 'Corinthians',
        'jogador': 'Yuri Alberto',
        'atacante': 80,
        'defensores': [75, 100, 78.5, 60],
        'bola': 60
    }

#crie um teste para a minha rota /sobre
def test_root_sobre():
    resposta = cliente.get('/sobre')
    assert resposta.status_code== 200
    assert resposta.json() =={'nome': 'VAR FUTEBOL', 'versao': '1.0'}

#teste para a rota do impedimento caso esteja impedido
#adicionei alguns intens pois mudei o dadosLance tambem, percebi que ficava muito cheio de codigo entao crie uma variavel la em cima e usei o .copy para diminuir
#-linha no codigo
def test_root_impedimento():
    lance = LANCE_VALIDO.copy()
    resposta = cliente.post('/impedimento', json =lance)
    assert resposta.status_code == 200
    assert resposta.json() == {'decisao': 'jogador impedido'}

#teste para a rota do impedimento caso esteja nao esteja impedido
#adicionei alguns intens pois mudei o dadosLance tambem, percebi que ficava muito cheio de codigo entao crie uma variavel la em cima e usei o .copy para diminuir
#-linha no codigo, porem aqui tenho que mudar pois nao esta impedido entao tenho que mudar o atacante
def test_root_nao_impedimento():
    lance = LANCE_VALIDO.copy()
    lance['atacante'] = 77
    resposta = cliente.post('/impedimento', json = lance)
    assert resposta.status_code == 200
    assert resposta.json() == {'decisao': 'jogador nao esta impedido'}

#teste para a rota impedimento caso tenha apenas um defensor
def test_root_um_defensor():
    resposta = cliente.post('/impedimento', json = {'atacante':77, 'defensores' : [75], 'bola': 60})
    assert resposta.status_code == 422

