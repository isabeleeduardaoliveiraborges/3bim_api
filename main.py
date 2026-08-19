from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import ProdutoDB, LivroDB
from schemas import ProdutoCreate, ProdutoResponse, LivroCreate, LivroResponse
from fastapi.middleware.cors import CORSMiddleware


# Cria as tabelas caso ainda não existam
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# PRODUTOS
# =========================

# GET /produtos
@app.get("/produtos", response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(ProdutoDB).all()


# POST /produtos
@app.post("/produtos", response_model=ProdutoResponse, status_code=201)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo_produto = ProdutoDB(**produto.dict())

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto


# GET /produtos/{id}
@app.get("/produtos/{produto_id}", response_model=ProdutoResponse)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = (
        db.query(ProdutoDB)
        .filter(ProdutoDB.id == produto_id)
        .first()
    )

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    return produto


# DELETE /produtos/{id}
@app.delete("/produtos/{produto_id}", status_code=204)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = (
        db.query(ProdutoDB)
        .filter(ProdutoDB.id == produto_id)
        .first()
    )

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    db.delete(produto)
    db.commit()


# PUT /produtos/{id}
@app.put("/produtos/{produto_id}", response_model=ProdutoResponse)
def atualizar_produto(
    produto_id: int,
    dados: ProdutoCreate,
    db: Session = Depends(get_db)
):
    produto = (
        db.query(ProdutoDB)
        .filter(ProdutoDB.id == produto_id)
        .first()
    )

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    produto.nome = dados.nome
    produto.preco = dados.preco
    produto.quantidade = dados.quantidade

    db.commit()
    db.refresh(produto)

    return produto


# =========================
# LIVROS
# =========================

# GET /Livros
@app.get("/Livros", response_model=list[LivroResponse])
def listar_livros(db: Session = Depends(get_db)):
    return db.query(LivroDB).all()


# POST /Livros
@app.post("/Livros", response_model=LivroResponse, status_code=201)
def criar_livro(livro: LivroCreate, db: Session = Depends(get_db)):
    novo_livro = LivroDB(**livro.dict())

    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)

    return novo_livro


# GET /Livros/{id}
@app.get("/Livros/{livro_id}", response_model=LivroResponse)
def obter_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = (
        db.query(LivroDB)
        .filter(LivroDB.id == livro_id)
        .first()
    )

    if livro is None:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado"
        )

    return livro


# DELETE /Livros/{id}
@app.delete("/Livros/{livro_id}", status_code=204)
def remover_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = (
        db.query(LivroDB)
        .filter(LivroDB.id == livro_id)
        .first()
    )

    if livro is None:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado"
        )

    db.delete(livro)
    db.commit()


# PUT /Livros/{id}
@app.put("/Livros/{livro_id}", response_model=LivroResponse)
def atualizar_livro(
    livro_id: int,
    dados: LivroCreate,
    db: Session = Depends(get_db)
):
    livro = (
        db.query(LivroDB)
        .filter(LivroDB.id == livro_id)
        .first()
    )

    if livro is None:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado"
        )

    livro.titulo = dados.titulo
    livro.autor = dados.autor
    livro.ano_publicacao = dados.ano_publicacao
    livro.preco = dados.preco

    db.commit()
    db.refresh(livro)

    return livro