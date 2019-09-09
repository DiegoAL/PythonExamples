'''
Created on 9 de set de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ORM_SQLAlchemy import createBD


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\m206255\eclipse-workspace\PythonExamples\ApoioReferenciasPython\ORM_SQLAlchemy\BancoDeTeste.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Funcionario (db.Model):
    __tablename__ = "Funcionario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30),nullable = True)
    cpf = db.Column(db.String(30), nullable = True)
    
def main():
    
    createBD
    
    db.create_all()
    
    #gravando um dado
    funcionario = Funcionario(id = 4, nome = 'Diego', cpf = '123')
    db.session.add(funcionario)
    db.session.commit()
    
    #imprimindo dados da tabela
    pes = Funcionario.query.all()
    
    for p in pes:
        print(f'ID: {p.id} | Nome: {p.nome} | CPF: {p.cpf}\n')

@app.route('/')
def index():
    main()
    return 'Executado'
    