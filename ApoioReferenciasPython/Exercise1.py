'''
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that 
they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and 
printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)
'''
import datetime


#Variables
name = ""
age = 0
year1000yo = 0
currentYear = datetime.datetime.now()
numberOfRepetitions = 1


#logic
print("Starting....")
name = input("Please enter with your name:\n")
age = int(input("Enter with your age:\n"))
numberOfRepetitions = int(input("How many times would you like to repeat the message?\n"))
if age >= 100 :
    print("Sorry, I can't help you...")    
else:
    year1000yo = (100 - int(age)) + int(currentYear.year)
    print(numberOfRepetitions * ("You " 
                                 + name + ", will are 100 \
                                 years old in " 
                                 + str(year1000yo) +"\n"))

print("See you later...")