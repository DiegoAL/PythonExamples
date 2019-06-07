'''
Created on 7 de jun de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
import requests
import json
    
#def
def getInformation(title):
    try:
        req= requests.get('http://www.omdbapxi.com/?apikey=8015f59e&t=' + title)
        dicionario = json.loads(req.text)
        return dicionario

    except Exception as err:
        return err

def printInformations(dicionario):
    #if 'Title' in dicionario
        print('Title:', dicionario['Title'])
        print('Released:', dicionario['Released'])
        print('Genre:', dicionario['Genre'])
        print('Actors:', dicionario['Actors'])
        print('IMDB Rating:', dicionario['imdbRating'])
    
#logic

printInformations(getInformation('Matrix'))
