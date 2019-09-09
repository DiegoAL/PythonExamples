'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

#var
inputText = ""
#isPalindrome = []

#logic
inputText = input("Type a text: ").replace(" ", "")
isPalindrome = inputText[::-1]

if inputText == isPalindrome :
    print("The text typed is a palindrome")
else:
    print("This text is not a palindrome!!!")


