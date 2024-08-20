from flask import Flask , render_template,request ,redirect,session

#instanciando
app = Flask(__name__,template_folder='./templates')

app.secret_key = "hadouken"

class Pessoa:
  def __init__(self,nome:str,cargo:str,stacks:str) -> None:
    self.nome = nome
    self.cargo = cargo
    self.stacks = stacks 
    

pessoa1 = Pessoa("Johnny","Full stack", "Python, JS")
pessoa2 = Pessoa("Fulano","Back End", "Python")
pessoa3 = Pessoa("Sicrana","Front End", " JS")

lista_pesssoas = [ pessoa1,pessoa2,pessoa3 ]


@app.route("/", methods = ['GET',])
def home():
  return render_template("index.html", pessoas = lista_pesssoas)

@app.route("/cadastro/")
def cadastrar():
  return render_template("cadastrar_time.html")

@app.route("/adicionar", methods = ['POST',])
def cadastrarPessoas():
  nome = request.form["nome"]
  cargo = request.form["cargo"]
  stacks = request.form["stacks"]

  novo_cadastro = Pessoa(nome=nome,cargo =cargo,stacks= stacks)

  lista_pesssoas.append(novo_cadastro)

  return redirect("/")

@app.route("/login", methods = ['get'])
def login():
  return render_template("login.html",)

@app.route("/autenticar", methods = ['POST',])
def autenticar():

  #seria armazenado na DB
  usuariodefault = "admin"
  senhadefault = "senha123"

  login = request.form["login"]
  senha = request.form["senha"]

  if login == usuariodefault and senhadefault == senha :
    session["usuario_logado"] = request.form[login]

    return redirect("/")
  else:
    return redirect("/falha")
  
@app.route("/falha",)
def falha():
  return render_template("falha.html")
    

@app.route("/logout")
def logout():
  session["usuario_logado"] = None
  return redirect("/login")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.errorhandler(400)
def bad_request(e):
    # note that we set the 400 status explicitly
    return render_template('400.html'), 400

@app.errorhandler(500)
def bad_request(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500

if __name__ == "__main__":
  app.run( debug = True)