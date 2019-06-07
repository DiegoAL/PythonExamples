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
        #TODO: Verificar o retorno das requisicoes para tratar erros
        print(dicionario)#####
        return dicionario

    except Exception as err:
        return err

def printInformations(dicionario):
    #TODO: Como trycatch não funciona pra esse caso validar os retornos e tratar com IFs
    #if 'Title' in dicionario:
        
        print('Title:', dicionario['Title'])
        print('Released:', dicionario['Released'])
        print('Genre:', dicionario['Genre'])
        print('Actors:', dicionario['Actors'])
        print('IMDB Rating:', dicionario['imdbRating'])
    #elif:
        
#logic

print(getInformation('Matrix'))


