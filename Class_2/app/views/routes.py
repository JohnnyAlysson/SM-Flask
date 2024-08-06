from flask import Flask , render_template

#instanciando
app = Flask(__name__,template_folder='../templates')

#definindo primeira rota
@app.route("/")
def home():
  return render_template("index.html")

@app.route("/<nome>")
def nome(nome):
  return f"Ola {nome}"

@app.route("/hello")
def hello():
  return "Hello World"