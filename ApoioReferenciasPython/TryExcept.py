'''
Created on 5 de jun de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''

import random
#def
def returnTrue():
    rngNumber = random.randint(10, 100)
    i = 0
    
    while i <= rngNumber:
        try:
            returnTrue(i)
        except Exception as err:
            print("Ocorreu erro", err)
        i+=1
        
def function1(param):
    if param == 5:
        return True
    else:
        return Exception

#var

returnTrue()

#logic
