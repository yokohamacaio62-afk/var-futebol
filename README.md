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

### Dia 1 (18/11/26)

#### Á Noite

- Criei minhas primeiras rotas com FastAPI
- Entendi cliente e servidor
- Fiz a regra do impedimento
- Aprendi o básico de Git e GitHub

---

### Dia 2 (19/11/26)

#### Pela Manha 
- Fiz o import de algumas coisas do logica_var para o main.py
- Criei uma class chamada DadosLance usando o basemodel
- E criando os atacantes como float e todos menos o defensores pois estavam em uma lista
- Apos usei post para o /impedimento aonde passei uma funcao root_impedimento usando uma variavel lance e tipo DadosLance retornando um dict decisao usando a funcao impedimento que importei e apenas colocando os atacantes defensores e etc

#### Á Noite

- usei o pytest para testar o impedimento
- usei pela primeira vez o assert que ele vai me mostrar quando eu errar e quando eu usar ele tem que ter sempre test \_
- Errei de proposito para ver se funcionava
- Criei 6 teste todos parecidos
- Entendi que o erro é 402 a culpa do que enviaram nao culpa do servidor (porem acho que se eu nao pensei a culpa foi minha)
- usei o Field com o min_length =2 para nao deixar a lista ser menos que 2 pois um seria o goleiro

---

### Dia 3 (19/11/26)

#### Pela Tarde

- usei o testclient como falso navegador
- entendi a diferenca entre testar uma funcao e testar a api
- que no test o cliente sempre sou eu entao eu passo as informacoes e o assert guarda a resposta que ja conheco
- que um teste nao calcula a resposta ela ja sabe qual e a reposta
- que nao arruma um teste antes para ele passar, primeiro descobre oque falhou

---

### Dia 4 (21/11/26)

#### Pela manhã
- Planejei o meu banco de dados: coloquei o que guardar de cada lance e qual tipo
- Aprendi o que é um banco relacional e linhas, colunas, tabela
- Aprendi o que é um ORM (que seria um tradutor do py para sql). Também aprendi as peças: motor engine, criação das tabelas
- Aprendi o que é chave e o que começa vazio antes de salvar
- Decidi guardar os defensores como texto usando json.dumps e json.loads
- Adicionei tempo, minuto, segundo para diferenciar lances no mesmo minuto
- Criei a classe Lance com SQLModel e o banco var.db com SQLite
- Vi o que o sql gerou com o echo=True
- Usei o git restore pois perdi um arquivo
- Coloquei os arquivos .db no .gitignore

---

### Dia 5 (22/11/26)

### Pela manhã
- Adicionei novos dados na DadosLance: jogo, data, tempo, minuto, segundo, time e jogador
- Entendi o que o ge, lt, gt e le do Field fazem para colocar limites
- Adicionei limites no tempo de 1 a 4 para caso tenha prorrogação, minuto de 0 a 130 e segundo de 0 a 59
- Usei max_length nos defensores pois só pode ter 11 em campo
- Aprendi o formato ISO
- Aprendi o princípio DRY e fiz o LANCE_VALIDO e o copy()

---

### Dia 6 (23/11/26)

#### Pela tarde
- Estudei o SQLModel
- Entendi como salvar no banco de dados: criar os objetos, abrir a session, add e commit
- Aprendi a usar o with
- Separei a decisão numa variável para usar ela duas vezes
- Criei um objeto Lance na rota com os dados que chegaram e a decisão
- Usei o json.dumps para poder guardar a lista de defensores
- Fiz a rota POST /impedimento salvar cada lance no banco de dados var.db
- Descobri que os testes estão salvando lances no banco de verdade

---

### Dia 7 (24/11/26)

#### Pela noite

- Estudei como buscar dados no banco com o SQLModel
- Aprendi o SELECT do SQL e que o * quer dizer todas as colunas
- Entendi os passos da consulta: abrir a session, montar o pedido com select, executar com exec e pegar a lista com .all()
- Criei a rota GET /lances para mostrar o histórico de lances
- Usei um for com model_dump, json.loads e append para devolver os defensores como lista
---

### Dia 8 (26/11/26)

#### Pela manhã

- Criei a rota GET /lances/{lance_id} para ver um lance específico pelo id
- Usei o session.get para buscar um lance pela chave primária
- Aprendi o código 404 (não encontrado) e usei o HTTPException para devolver ele
- Entendi a diferença entre o raise, que para tudo na hora, e o return
- Criei a função formatar_lance para não repetir código nas duas rotas
- Testei no /docs: com o id 1 deu 200 e com o 999 deu 404