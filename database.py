from sqlmodel import Field, SQLModel
from datetime import date

class Lance(SQLModel, table =True):
    id: int | None =Field(default=None, primary_key=True)
    jogo : str
    data : date
    tempo : int
    minuto : int
    segundo : int
    time : str 
    jogador : str
    atacante : float 
    defensores : str    
    bola : float 
    decisao : str 
