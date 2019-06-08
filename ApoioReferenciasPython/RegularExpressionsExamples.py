'''
Created on 7 de jun de 2019

@author: Diego Alves A. (diego.assis@enel.com)

DOCUMENTACAO DE APOIO:

    https://docs.python.org/3.6/library/re.html?highlight=regular%20expression
    https://regex101.com/

'''
import re

# O r transforma o texto em RAW String
# RAW String pega os caracteres especiais e tira
# Tira os "Enter"
# Colocamos o r para o caracter especial  deixar de ser especial
# O ponto equivale a qualquer caracter r'Gat.'
# O \W coloca letras, não considera espaço vazio
# \W \W \W \W procura qual palavra tem quatro letras
# Depois do Gat pode ter uma ou mais letras
# Repete o padrão
# O asterisco pode ter 0 ou mais
# \. é para ver se tem um ponto


aText = 'Ola mundooo outra vez loucuraaa mundana diego.assis@enel.com'

#Qualquer palavra depois da expressao, seleciona a primeira ocorrencia
aregex = re.search(r'mund.', aText) #Raw String
print(aregex.group())
print('---')

#two characters
aregex = re.search(r'out\w\w', aText) #Raw String
print(aregex.group())
print('---')

#pegando todas as ocorrencias na frase
bregex = re.findall(r'mund\w', aText)
print(bregex)
print('---')

#toda as ocorrencias da frase com texto completo
# +-> todas as ocorrencias + o re
# * -> todas as ocorrencias
bregex = re.findall(r'mund\w+', aText)
print(bregex)
print('---')

#a email
pegar_email = "fafsefsefef " \
              "sfsefsefsef " \
              "diego.assis@enel.com" \
              "sfesefsef "\
              "asef84-fees@eneef-fe.co-m.fex "
                
padrao_email = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', pegar_email)
print(padrao_email)
print('---')
