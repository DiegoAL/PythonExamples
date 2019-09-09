    '''
Take two lists, say for example these two:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are 
common between the lists (without duplicates). Make sure your program 
works on two lists of different sizes. Write this using at least one list comprehension. 
(Hint: Remember list comprehensions from Exercise 7)

Extra:

1. Randomly generate two lists to test this

https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
'''
import random

#var
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = [random.randint(0,30) for x in range(random.randint(5,15))]
b = [random.randint(0,30) for x in range(random.randint(5,15))]
allElements = [lstA for lstA in list(dict.fromkeys(a)) for lstB in 
               list(dict.fromkeys(b)) if lstA == lstB]
'''
#Another way to solve the same exercise 
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in a if i in b]
'''

print("List A: " + str(a))
print("List B: " + str(b))
print("Commons List: " + str(allElements))
    
    