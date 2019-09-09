'''
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions.

https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
'''
#def
def inputNumber(_text = "Type a number "):
    return int(input(_text))

def isPrime(_number = 0):
    _divisor = 2
    _allDivisors = []
    _msgYes = "This number is Prime!"
    _msgNo = "This number is not prime"
    
    if _number > 1:
        while _divisor < _number :
            if _number % _divisor == 0:
                _allDivisors.append(_divisor)
            _divisor += 1            
        if not _allDivisors:
            return _msgYes   
        else:
            return _msgNo
    else:
        return _msgNo
#var
_userInput = ""

#logic
_userInput = inputNumber()
print(isPrime(_userInput))
