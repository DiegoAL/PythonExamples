'''
Created on 6 de set de 2019

@author: Diego Alves A. (diego.assis@gmail.com)

'''

import sqlite3
import io

#Realiza a conexão com o banco de dados, caso não exista criando a tabela 
conn = sqlite3.connect('clientes.db')

#cursor: é um interador que permite navegar e manipular os registros do bd.
#execute: lê e executa comandos SQL puro diretamente no bd.

cursor = conn.cursor()

#CREATE TABLE

#criando uma tabela
cursor.execute("""
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf     VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        criado_em DATE NOT NULL
);
""")


#INSERT

#inserindo dados em uma tabela de forma unitaria
cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Regis', 35, '00000000000', 'regis@email.com', '11-98765-4321', 'Sao Paulo', 'SP', '2014-06-08')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Aloisio', 87, '11111111111', 'aloisio@email.com', '98765-4322', 'Porto Alegre', 'RS', '2014-06-09')
""")

# inserindo dados na tabela com base em uma lista
# criando uma lista de dados
lista = [(
    'Fabio', 23, '44444444444', 'fabio@email.com', '1234-5678', 'Belo Horizonte', 'MG', '2014-06-09'),
    ('Joao', 21, '55555555555', 'joao@email.com',
     '11-1234-5600', 'Sao Paulo', 'SP', '2014-06-09'),
    ('Xavier', 24, '66666666666', 'xavier@email.com', '12-1234-5601', 'Campinas', 'SP', '2014-06-10')]

#gravando a lista
cursor.executemany("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", lista)

# inserindo dados digitados pelo usuario
p_nome = input('Nome: ')
p_idade = input('Idade: ')
p_cpf = input('CPF: ')
p_email = input('Email: ')
p_fone = input('Fone: ')
p_cidade = input('Cidade: ')
p_uf = input('UF: ')
p_criado_em = input('Criado em (yyyy-mm-dd): ')

# inserindo os dados especificando os campos
cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", (p_nome, p_idade, p_cpf, p_email, p_fone, p_cidade, p_uf, p_criado_em))

# Apenas após o commit que os dados realmente são gravados no banco
conn.commit()


#READ/SELECT

# Realizando uma consulta no banco de dados
cursor.execute("""
SELECT * FROM clientes;
""")

#não é necessario amarzenar os dados em uma variavel, pois o método "fetchall" retorna o resultado da consulta
for linha in cursor.fetchall():
    print(linha)


#UPDATE

#Vavriaveis com valores novos
id_cliente = 1
novo_fone = '11-1000-2014'
novo_criado_em = '2014-06-11'

# alterando os dados da tabela
cursor.execute("""
UPDATE clientes
SET fone = ?, criado_em = ?
WHERE id = ?
""", (novo_fone, novo_criado_em, id_cliente))

conn.commit()


#DELETE

#ID que será excluido
id_cliente = 8

# excluindo um registro da tabela
cursor.execute("""
DELETE FROM clientes
WHERE id = ?
""", (id_cliente,))

conn.commit()


#ALTER TABLE

# adicionando uma nova coluna na tabela clientes
cursor.execute("""
ALTER TABLE clientes
ADD COLUMN bloqueado BOOLEAN;
""")

conn.commit()


#OTHER

nome_tabela = 'clientes'

# obtendo informações da tabela
cursor.execute('PRAGMA table_info({})'.format(nome_tabela))

colunas = [tupla[1] for tupla in cursor.fetchall()]
print('Colunas:', colunas)
# ou
# for coluna in colunas:
#    print(coluna)

# listando as tabelas do bd
cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
""")

print('Tabelas:')
for tabela in cursor.fetchall():
    print("%s" % (tabela))

# obtendo o schema da tabela
cursor.execute("""
SELECT sql FROM sqlite_master WHERE type='table' AND name=?
""", (nome_tabela,))

print('Schema:')
for schema in cursor.fetchall():
    print("%s" % (schema))


#BACKUP

#Realizando o backup do banco

#O metodo "io.open" que salva os dados num arquivo externo através do método write
#O método "iterdump" exporta a estrutura e dados da tabela para o arquivo externo
with io.open('clientes_dump.sql', 'w') as f:
    for linha in conn.iterdump():
        f.write('%s\n' % linha)

print('Backup realizado com sucesso.')
print('Salvo como clientes_dump.sql')

#Restaurado um backup de banco de dados

#realiznado a criação de numo novo banco de dados
conn_Novo = sqlite3.connect('clientes_recuperado.db')
cursor_Novo = conn_Novo.cursor()

f = io.open('clientes_dump.sql', 'r')

#O método "read" lê o conteúdo do arquivo clientes_dump.sql
sql = f.read()

#método "executescript" executa as instruções SQL escritas no arquivo de backup
cursor_Novo.executescript(sql)

print('Banco de dados recuperado com sucesso.')
print('Salvo como clientes_recuperado.db')

conn_Novo.close()

#Sempre inportante encerrar uma conexão 
conn.close()