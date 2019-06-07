'''
Created on 6 de jun de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
import requests

req_head = {'User-agent' : 'Windows 20.1', 
            'Referer' : 'https://google.com'}

req_cookie = {'ultimaVisita' : '11-11-2020',
              'primeiroAcesso' : '01-01-2017'}

req_body = {'user' : 'DiegoA',
              'password' : '1234566'}

try:
    myRequest = requests.post('https://putsreq.com/GMljvJaBBTTYk3SuE67y', 
                             headers = req_head,
                             cookies = req_cookie,
                             data = req_body)
    print(myRequest.text)
except Exception as err:
    print(err)