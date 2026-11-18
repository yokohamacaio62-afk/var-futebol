# ⚽ VAR Futebol

Gosto muito de futebol e decidir tentar criar um var.
Ainda estou no começo, aprendendo enquanto construo.

## O que já fiz
- Regra do impedimento funcionando
- API inicial com FastAPI

## Próximos passos
- Ligar a regra à API
- Analisar imagens dos lances

## Como funciona o impedimento no código
O campo é uma régua de 0 a 105 metros. É impedimento quando o atacante está
na frente do penúltimo defensor, na frente da bola e no campo do adversário,
tudo ao mesmo tempo.

## Tecnologias
Python, FastAPI, Uvicorn, Git

## Como rodar
pip install fastapi uvicorn
uvicorn main:app --reload

## Diário
### Dia 1
- Criei minhas primeiras rotas com FastAPI
- Entendi cliente e servidor
- Fiz a regra do impedimento
- Aprendi o básico de Git e GitHub
