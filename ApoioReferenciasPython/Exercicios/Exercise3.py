'''
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

1. Instead of printing the elements one by one, 
make a new list that has all the elements less than 5 from this list in it and 
print out this new list.

2. Write this in one line of Python.

3. Ask the user for a number and return a list that contains only elements from 
the original list a that are smaller than that number given by the user.

https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
'''

#var
var_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
var_list5 = []
number = 0

#1 solution
'''
for element in var_list:
    if element < 5 :
        var_list5.append(element)
    else :
        break

for element in var_list5:
    print(element)
'''
    
#2 solution
#print([element for element in var_list if element < 5])    
  
#3 solution
number = int(input("Type a number\n"))
for element1 in var_list :
    if int(element1) < number :
        print(element1)