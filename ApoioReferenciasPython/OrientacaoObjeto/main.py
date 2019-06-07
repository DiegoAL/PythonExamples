'''
Created on 4 de jun de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
#def
from OrientacaoObjeto.Conta import Conta


#var


#logic
conta1 = Conta('Diego', 4321234, 12, 300, 1000)
print('Saldo atual: ', conta1.consultaSaldo())

conta1.sacar(float(input('Valor para sacar: ')))

print('Saldo atual: ', conta1.consultaSaldo())

conta1.depositar(float(input('Valor para deposito: ')))

print('Saldo atual: ', conta1.consultaSaldo())


