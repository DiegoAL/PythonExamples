'''
Created on 7 de jun de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
import requests
import json
    
#def
def getInformation(title):
    try:
        req= requests.get('http://www.omdbapi.com/?apikey=292834bb&t=' + title)
        dicionario = json.loads(req.text)
        print(dicionario)#####
        return dicionario

    except Exception as err:
        return err

def printInformations(dicionario):   
        print('Title:', dicionario['Title'])
        print('Released:', dicionario['Released'])
        print('Genre:', dicionario['Genre'])
        print('Actors:', dicionario['Actors'])
        print('IMDB Rating:', dicionario['imdbRating'])

#logic

print(getInformation('Matrix'))


