# schemas.py
from pydantic import BaseModel
 
class ProdutoBase(BaseModel):
    nome: str
    preco: float
    quantidade: int
   
class ProdutoCreate(ProdutoBase):
    pass
 
class ProdutoResponse(ProdutoBase):
    id: int
   
    class Config:
        from_attributes = True
 
 
class LivroBase(BaseModel):
    titulo: str
    preco: float
    ano_publicacao: int
    autor: str
     
class LivroCreate(LivroBase):
    pass
 
class LivroResponse(LivroBase):
    id: int
   
    class Config:
        from_attributes = True