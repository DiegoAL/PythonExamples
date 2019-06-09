'''
Created on 9 de jun de 2019

@author: Diego
'''

import oauth2
import json
import urllib.parse

#Parametros obtidos na API
consumer_key = 'xxxxx'
consumer_secret = 'xxxxx'
token_key = 'xxxxxF'
token_secret = 'Cxxxxxx'

#Methodo de autenticacao ouath2 utilizado pela API
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Pesquisa: ")
#Metodo para deixar uma string codificada em html
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)
twittes = objeto['statuses']

for twit in twittes:
    print(twit['user']['screen_name'])
    print(twit['text'])
    print()