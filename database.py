from sqlmodel import Field, SQLModel,create_engine
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

sqlite_file_name = "var.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)