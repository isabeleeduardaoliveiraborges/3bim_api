from fastapi import FastAPI
app=FastAPI(title="minha primeira API")
@app.get('/')
def principal():
    return{'mensagem':'minha primeira API em FastAPI!'}

@app.get('/sobre')
def sobre():
    return{'mensagem':'pagina sobre'}