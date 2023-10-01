# The simplest kind of if statement has one test and one action:

# age = 19
# if age >= 18:
#  print("You are old enough to vote!")
#  print("Have you registered to vote yet?")
#  if age is old enough python will run it if not it ingores it
# If the value of age is less than 18, this program would produce no
# output.

age = 19
if age >= 18:
 print("You are old enough to vote!")
 print("Have you registered to vote yet?")


else:
  print("Sorry, you are too young to vote.")
  print("Please register to vote as soon as you turn 18!")
# If the conditional test at 1 passes, the first block of indented print
# statements is executed. If the test evaluates to False, the else block at v is
# executed. Because age is less than 18 this time, the conditional test fails and
# the code in the else block is executed

# elif statement
# •	 Admission for anyone under age 4 is free.
# •	 Admission for anyone between the ages of 4 and 18 is $5.
# •	 Admission for anyone age 18 or older is $10
# age = 12
# if age < 4:
#   print("your admission is $0.")
# elif age < 18:
#   print("your admissions cost is $5.")
# else:
#   print("your admissions cost is $10")


# age = 12
# if age < 4:
#  price = 0
# elif age < 18:
#  price = 5
# else:
#  price = 10
# print("Your admission cost is $" + str(price) + ".")

#  it simply determines the admission price.
# In addition to being more efficient, this revised code is easier to modify
# than the original approach. To change the text of the output message, you
# would need to change only one print statement rather than three separate
# print statements.

age = 12
if age < 4:
 price = 0
elif age < 18:
 price = 5
elif age < 65:
 price = 10
elif age < 65:
 price = 5
print("Your admission cost is $" + str(price) + ".")

# Testing Multiple Conditions

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
 print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
 print("Adding extra cheese.")

print("\nFinished making your pizza!")
# However, sometimes it’s important to check all of the conditions of
# interest. In this case, you should use a series of simple if statements with no
# elif or else blocks. This technique makes sense when more than one condition could be True, and you want to act on every condition that is True.

# special iteams
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#  print("Adding " + requested_topping + ".")
# print("\nFinished making your pizza!")
#  simple loop

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
 if requested_topping == 'green peppers':
  print("Sorry, we are out of green peppers right now.")
 else:
  print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

# ^ This time we check each requested item before adding it to the pizza.
# The code at u checks to see if the person requested green peppers. If so,
# we display a message informing them why they can’t have green peppers.
# The else block at v ensures that all other toppings will be added to the
# pizza.

# checking a empty list
requested_toppings = []
if requested_toppings:
 for requested_topping in requested_toppings:
   print("Adding " + requested_topping + ".")
 print("\nFinished making your pizza!")
else:
 print("Are you sure you want a plain pizza?")
# ^ an empty list evaluates to False so then it print the else

# multiple list
available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
 if requested_topping in available_toppings:
  print("Adding " + requested_topping + ".")
 else:
  print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")