from flask import Flask


app = Flask("app")

# view / rota
@app.route("/")
def hello():
    return "<h1> Ola Mundo, <strong> estou aprendendo o framework Flask </strong> </h1> ", 200

@app.route("/uepg")
@app.route("/deinfo")
def uepg():
    return "<h3> Ola UEPG </h3>"

@app.route("/deinfo/<nome>")
def deinfo_nome(nome):
    if nome.lower() == "luciano":
        return  "Ola {}".format(nome), 200
    else:
        return "Nao encontrado", 404 
    
