'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and 
makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.

https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
'''
#def
def firtsAndLast(_array = []):
    if len(_array) > 2:        
        return [_array[0], _array[len(_array) - 1]]
    else:
        return _array

#logic
_lista = [1,5,6,7,5,3]
print(firtsAndLast(_lista))