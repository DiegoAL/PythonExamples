'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,  
too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras
1. Keep the game going until the user types 'exit'
2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random

#var
_rngNumber = 0
_usrNumber = ""
_usrTrack = 0

#logic
while True:
    _rngNumber =  random.randint(1,9)
    _usrNumber = input("\nType a number or exit: ").lower()
        
    if _usrNumber == "exit" :
        print("You try guess " + str(_usrTrack) + " time(s)")
        break
    else:
        _usrNumber = int(_usrNumber)
        if _usrNumber < _rngNumber :
            print("Your guessed is wrong, too low")
        
        elif _usrNumber > _rngNumber :
            print("Your guessed is wrong, too high")
            
        else:
            print("Your guessed is exactly right")
 
        _usrTrack += 1


