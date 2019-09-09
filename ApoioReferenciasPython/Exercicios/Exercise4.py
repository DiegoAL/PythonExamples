'''
Create a program that asks the user for a number and then prints out a list of all 
the divisors of that number. (If you dont know what a divisor is, 
it is a number that divides evenly into another number. For example, 
13 is a divisor of 26 because 26 / 13 has no remainder.)

https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

**To create a list of numbers from 2 to 10, just use the following code:
  x = range(2, 11)
'''

#var
number = 0
divisor = 1
listOfDivisors = []

#logic
number = int(input("Type a number: "))

while divisor <= number :
    if number % divisor == 0 :
        listOfDivisors.append(divisor)
    
    divisor += 1 

print(str(listOfDivisors)) 
