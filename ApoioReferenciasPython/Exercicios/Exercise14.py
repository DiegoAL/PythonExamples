'''
Write a program (function!) that takes a list and returns a new list 
that contains all the elements of the first list minus all the duplicates.

Extras:

1. Write two different functions to do this - one using a loop and 
constructing a list, and another using sets.

2. Go back and do Exercise 5 using sets, and write the solution for that in 
a different function.

https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
'''

#def
def listWithouDuplicates(_alist = []):
    return list(dict.fromkeys(_alist))

#var
_alist1 = [2,3,55,665,3,5,6,7,88,8,8,9,9,3,2,1]
_alist1.sort()

#logic
print(listWithouDuplicates(_alist1))