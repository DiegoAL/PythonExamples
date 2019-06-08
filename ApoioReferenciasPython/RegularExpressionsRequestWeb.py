'''
Created on 7 de jun de 2019

@author: Diego

Detalhes nos outro arquivo
'''

import requests
import re

varLocation = input('Diga um lugar para verificar a previsão do tempo: ')
vReqCotacao = requests.get('https://economia.uol.com.br/cotacoes/')
#TODO: tratar requisiçoes que envolver espaço tipo Sao+Paulo
vReqWheather = requests.get('https://www.google.com/search?q=previs%C3%A3o+do+tempo+para+' + varLocation)

cotacao = re.search(r'R\$ [1-9],[1-9]*',vReqCotacao.text)
#TODO: Regex n esta ok
forecast = re.search(r'id\=\"wob_tm\".*\<',vReqWheather.text)

print ('A cotação atual do dolar é:', cotacao.group())
print('A previsão do tempo para cidade selecionada é:', forecast.group())

