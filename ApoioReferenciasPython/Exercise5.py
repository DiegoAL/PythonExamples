'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are 
common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this

'''
import random

#var
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
commonsList = []

#logic
for temp in range(5):
    a.append(random.randint(1,200))
    b.append(random.randint(1,200))

commonsList = list(dict.fromkeys(a))

for item in b:
    if item not in commonsList:
        commonsList.append(item)

commonsList.sort()
print(commonsList)
