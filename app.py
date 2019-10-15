from flask import Flask


app = Flask("app")

# view / rota
@app.route("/")
def hello():
    return "<h1> Ola Mundo, <strong> estou aprendendo o framework Flask </strong> </h1> ", 200
    
