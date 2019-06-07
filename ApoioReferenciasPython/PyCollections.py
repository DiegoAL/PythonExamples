'''
Created on 30 de mai de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''

#List
#Lista dinamica que permite CRUD

#-> iniciando com dados
_lista = ['abc', 1, 3.5, True]

# -> iniciando vazio
_lista2 = []

#Tupla / tuple
#è uma lista com itens fixos, que não permite alteracoes futuras

#-> iniciando com dados
_tupla = (3, False, "teste")

# -> iniciando vazio
_tupla2 = ()

#Dicionario / Dict
#é um dicionario, divido em key e value, tem maior eficiencia em buscas e não possui ordem (index)

#-> iniciando com dados
_dictionary = {'nome' : 'Diego', 'Idade' : 25}
print(_dictionary['nome'])

# -> iniciando vazio
_dictionary2 = {} #or_dictionary2 = dict() 

#Conjunto/ set
#È a mistura da lista com o dicionario, não permite valores duplicados e não usa a key alem de não ter odenação (index). Ele é um tabela hash

#-> iniciando com dados
_conjunto = {'Diego', 'Franciele', 'Joao','Diego'}
print(_conjunto)

# -> iniciando vazio
_conjunto2 = set()
