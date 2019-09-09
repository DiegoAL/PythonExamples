'''
Write a password generator in Python. Be creative with how you generate 
passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

'''
#def
import string
import random

def getNewPsw(pswSize):
    newPassword = ''
    listOfWordsLower = list(string.ascii_lowercase)
    listOfWordsUpper = list(string.ascii_uppercase)
    listOfNumbers = range(0,10)
    listOfSymbols = ('#', "@", '!', '$', '%', "*")
    
    listofLists = (listOfNumbers, listOfSymbols, listOfWordsLower, listOfWordsUpper)
    
    while not pswSize == 0:
        rngColunm = random.randint(0,3)
        rngValue = random.randint(0, len(listofLists[rngColunm]) - 1)
        newPassword += str(listofLists[rngColunm][rngValue])      
        pswSize -= 1
        
    return newPassword


#var
print(getNewPsw(15))

#logic
