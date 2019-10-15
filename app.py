from flask import Flask, request, render_template

app = Flask("app")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("form.html")
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['passwd']
        return u"Olá {}, sua senha é: {}".format(nome,senha)


# view / rota
@app.route("/")
def hello():
    return "Ola Mundo por meio do método {}".format(request.method)
    
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
    

        