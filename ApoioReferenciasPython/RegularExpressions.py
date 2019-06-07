'''
Created on 7 de jun de 2019

@author: Diego Alves A. (diego.assis@enel.com)

DOCUMENTACAO DE APOIO:

    https://docs.python.org/3.6/library/re.html?highlight=regular%20expression

'''
import re

aText = 'Ola mundooo outra vez loucuraaa mundana diego.assis@enel.com'

#Qualquer palavra depois da expressao
aregex = re.search(r'mund.', aText) #Raw String
print(aregex.group())

#two characters
aregex = re.search(r'out\w\w', aText) #Raw String
print(aregex.group())

#a email
aregex = re.search(r'.@.\w\w\w\.', aText) #Raw String
print(aregex.group())
