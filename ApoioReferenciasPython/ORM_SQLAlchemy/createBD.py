'''
Created on 9 de set de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
import sqlite3

def __init__():
    connect = sqlite3.connect('BancoDeTeste.db')
    connect.close()
