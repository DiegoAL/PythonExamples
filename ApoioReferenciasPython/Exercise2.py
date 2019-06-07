'''
Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.

2. Ask the user for two numbers: one number to check (call it num) and one number to
divide by (check). If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.
'''

# var
number = 0
check = 0

# logic
number = int(input("Type a number!\n"))
check = int(input("Type a divisor!\n"))

if number % 2 == 0 :
    if number % 4 == 0:
        print("This number is a multiple of 4")
    else:             
        print("This number is even!")
else:
    print("this number is odd!")

if number % check == 0 :
    print(str(number) + " is a multiple of " + str(check))
else:
    print(str(number) + " is not multiple of " + str(check) + "\nTry Again...")
