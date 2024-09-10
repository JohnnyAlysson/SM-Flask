from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True  

app.config["SQLALCHEMY_DATABASE_URI"] = \
  '{SGBD}://{user}:{password}@{server}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    user = 'root',
    password = '',
    server = 'localhost',
    database = 'turma'
  )

db = SQLAlchemy(app)

class Aluno(db.Model):
  __tablename__ = 'alunos'

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  nome = db.Column(db.String(100), nullable=False)
  email= db.Column(db.String(100), nullable= True)

  def to_json(self):
    return{
      'id': self.id,
      'nome' : self.nome,
      'email' : self.email,
    }

class Professores(db.Model):

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  nome = db.Column(db.String(100), nullable=False)
  email= db.Column(db.String(100), nullable= False)


with app.app_context():
  db.create_all()



@app.route('/alunos',methods=['GET'])
def selecionar_alunos():
  alunos = Aluno.query.all()
  alunos_json = [aluno.to_json() for aluno in alunos]
  return gerar_response(
    status= 200,
    nome_conteudo= 'Aluno',
    conteudo= alunos_json,
    mensagem= "ok"
  )



@app.route('/alunos/<id>',methods=['GET'])
def selecionar_aluno(id):
  aluno = Aluno.query.filter_by(id=id).first()
  aluno_json = aluno.to_json()
  return gerar_response(
    status= 200,
    nome_conteudo= 'Aluno',
    conteudo= aluno_json,
    mensagem= "ok"
  )


@app.route('/alunos',methods=['POST'])
def criar_alunos():
  body =request.get_json()

  try:
    aluno = Aluno(nome=body['nome'],email = body['email'])
    db.session.add(aluno)
    db.session.commit()
    return gerar_response(
      "201",
      "Aluno",
      aluno.to_json(),
      "aluno criado com sucesso"
    )
  except Exception:
    return gerar_response(400,'Aluno',{}, "Erro ao cadastrar aluno")


@app.route('/alunos/<id>',methods=['PUT'])
def atualizar_alunos(id):

  aluno = Aluno.query.filter_by(id=id).first()
  body =request.get_json()

  try:
    if 'nome' in body:
      aluno.nome= body['nome']
    if 'email' in body:
      aluno.email = body['email']
    
    db.session.add(aluno)
    db.session.commit()
    return gerar_response(
      "200",
      "Aluno",
      aluno.to_json(),
      "aluno atualizado com sucesso"
    )
  except Exception:
    return gerar_response(400,'Aluno',{}, "Erro ao cadastrar aluno")
  

@app.route('/alunos/<id>',methods=['DELETE'])
def deletar_alunos(id):

  aluno = Aluno.query.filter_by(id=id).first()


  try:
    
    db.session.delete(aluno)
    db.session.commit()
    return gerar_response(
      "202",
      "aluno",
      aluno.to_json(),
      "aluno deletado com sucesso"
    )
  except Exception:
    return gerar_response(400,'Aluno',{}, "Erro ao deletar aluno")



#função para gerar reponse diferente ao cliente
def gerar_response(status,nome_conteudo,conteudo,mensagem = False):
  body = {}
  body['nome_conteudo'] = conteudo

  if mensagem:
    body['mensagem'] = mensagem

  return Response(
    json.dumps(body),
    status = status,
    mimetype= "aplication/json"
  )  






if __name__== "__main__":
  app.run(debug=True)

