'''
Created on 4 de jun de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''

import sys

def concat(text1, text2):
    return text1 + text2

def soma(n1, n2):
    return n1 + n2

#O primeiro argumento sempre sera o caminho do programa
# para passar um argumento o programa deve ser executado via terminal

argumentoExterno = sys.argv

if argumentoExterno[1] == 'concat':
    print(concat(argumentoExterno[2], argumentoExterno[3]))
elif argumentoExterno[1] == 'soma':
    print(soma(float(argumentoExterno[2]), float(argumentoExterno[3])))
else:
    print('Warning: Invalid option!!')
