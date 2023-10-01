# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
#  use of input() fuction

# name = input("please enter your name:  ")
# print("Hello + " + name + "!")

# prompt = " if you tell us who you are, we can personalize the message you see"
# prompt += "\nWhat is your name?" 
# name = input(prompt)
# print("\nHello, " + name + "!")
# ^^^
# This example shows one way to build a multi-line string. The first line
# stores the first part of the message in the variable prompt. In the second line,
# the operator += takes the string that was stored in prompt and adds the new
# string onto the end.
# The prompt now spans two lines, again with space after the question
# mark for clarity

# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 36:
#  print("\nYou're tall enough to ride!")
# else:
#  print("\nYou'll be able to ride when you're a little older.")

#  The program can compare height to 36 because height = int(height)
# converts the input value to a numerical representation before the comparison is made. If the number entered is greater than or equal to 36, we tell
# the user that they’re tall enough:

# The Modulo Operator
# print(4 % 3)

# even_or_odd
# number = input("Enter a number, I'll tell you if it is even or odd:  ")
# number = int(number)
# if number % 2 == 0:
#     print("\nThe number " + str(number) + " is even")
# else:
#     print("\nThe numberm " + str(number) + "is odd")

# WHILE LOOPS
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# In the first line, we start counting from 1 by setting the value of
# current_number to 1. The while loop is then set to keep running as long
# as the value of current_number is less than or equal to 5. The code inside
# the loop prints the value of current_number and then adds 1 to that value
# with current_number += 1. (The += operator is shorthand for current_number =
# current_number + 1.)
# Python repeats the loop as long as the condition current_number <= 5
# is true. Because 1 is less than 5, Python prints 1 and then adds 1, making the current number 2. Because 2 is less than 5, Python prints 2
# and adds 1 again, making the current number 3, and so on. Once the
# value of current_number is greater than 5, the loop stops running and the
# program ends

