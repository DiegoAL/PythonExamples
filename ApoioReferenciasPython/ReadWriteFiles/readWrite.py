'''
Created on 5 de jun de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
import random
file1 = open('TestFilex.txt', 'r+')

print(file1.read())

print('---')

for i in range(0,101):
    file1.write(str(random.randint(0,100)) + "\n")
    

for linha in file1:
    print(linha)
    
    
