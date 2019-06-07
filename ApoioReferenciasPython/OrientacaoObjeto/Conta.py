'''
Created on 4 de jun de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
from OrientacaoObjeto.Cliente import Cliente

class Conta (Cliente):
    def __init__(self,nome, cpf, idade, saldo, limite):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.saldo = saldo
        self.limite = limite
    
    def sacar(self, valorSacar):
        if self.saldo > 0 and valorSacar <= self.saldo:
            self.saldo -= valorSacar
    
    def depositar(self, valorDeposito):
        self.saldo += valorDeposito
    
    def consultaSaldo(self):
        return self.saldo
            
