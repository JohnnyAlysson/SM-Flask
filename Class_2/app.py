from flask import Flask , render_template,request

#instanciando
app = Flask(__name__,template_folder='./templates')

class Pessoa:
  def __init__(self,nome:str,cargo:str,stacks:str) -> None:
    self.nome = nome
    self.cargo = cargo
    self.stacks = stacks 
    

pessoa1 = Pessoa("Johnny","Full stack", "Python, JS")
pessoa2 = Pessoa("Fulano","Back End", "Python")
pessoa3 = Pessoa("Sicrana","Front End", " JS")

lista_pesssoas = [ pessoa1,pessoa2,pessoa3 ]
#definindo primeira rota
@app.route("/", methods = ['GET',])

def home():

  
  return render_template("index.html", pessoas = lista_pesssoas)

@app.route("/cadastro/")
#render
def cadastrar():
  return render_template("cadastrar_time.html")

@app.route("/adicionar", methods = ['POST',])
#função para cadastrar
def cadastrarPessoas():
  nome = request.form["nome"]
  cargo = request.form["cargo"]
  stacks = request.form["stacks"]

  novo_cadastro = Pessoa(nome=nome,cargo =cargo,stacks= stacks)

  lista_pesssoas.append(novo_cadastro)

  return render_template("index.html", pessoas= lista_pesssoas)

if __name__ == "__main__":
  app.run( debug=True)