# VAR Futebol

Gosto muito de futebol, Resolvi criar um VAR para aprender backend na prática.

Ainda estou no começo

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

#### Á Noite
- Criei minhas primeiras rotas com FastAPI
- Entendi cliente e servidor
- Fiz a regra do impedimento
- Aprendi o básico de Git e GitHub

### dia 2 

#### Pela Manha 
- Fiz o import de algumas coisas do logica_var para o main.py
- Criei uma class chamada DadosLance usando o basemodel
- E criando os atacantes como float e todos menos o defensores pois estavam em uma lista
- Apos usei post para o /impedimento  aonde passei uma funcao root_impedimento usando uma variavel lance e tipo DadosLance retornando um dict decisao usando a funcao impedimento que importei e apenas colocando os atacantes defensores e etc
