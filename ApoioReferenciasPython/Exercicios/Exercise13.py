'''
Write a program that asks the user how many Fibonnaci numbers to generate and 
then generates them. Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci sequence is a sequence of numbers where the next number 
in the sequence is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13...)

https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
'''
#def
def generateFibo(_maxSequence = 0):
    _fibonacci = []
    _counter = 1
    
    while _counter <= _maxSequence:
        if len(_fibonacci) < 2:
            _fibonacci.append(1)
        else :
            _fibonacci.append(_fibonacci[len(_fibonacci)-1] + _fibonacci[len(_fibonacci)-2])
        _counter += 1
        
    return _fibonacci

#var
_usrNumbers = 0

#logic
_usrNumbers = int(input("How many fibonacci numbers would you like to generate?"))
print(generateFibo(_usrNumbers))
