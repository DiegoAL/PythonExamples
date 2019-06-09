'''
Created on 7 de jun de 2019

@author: Diego

Detalhes nos outro arquivo
'''

import requests
import re
import json

###Using Regex####
vReqCotacao = requests.get('https://economia.uol.com.br/cotacoes/')
cotacao = re.search(r'R\$ [1-9],[1-9]*',vReqCotacao.text)
print ('A cotação atual do dolar é:', cotacao.group())


###Using API###
cidade = input("Previsão para qual cidade?: ")
APIKEY = 'e290bbf2007bd65bf9457bf47ac50fef'

forecast = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + cidade +'&units=metric&lang=pt' + '&APPID=' + APIKEY)
retorno = json.loads(forecast.text) 

print('Previsão de:', retorno['weather'][0]['description'])
print('Temperatura de:', retorno['main']['temp'])

