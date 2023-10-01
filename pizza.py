# Importing an Entire Module

def make_pizza(size, *toppings):
 """Summarize the pizza we are about to make."""
 print("\nMaking a " + str(size) +
 "-inch pizza with the following toppings:")
 for topping in toppings:
  print("- " + topping)
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# import function
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# The general syntax for providing an alias is:
# from module_name import function_name as fn


# Using as to Give a Module an Alias

import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import*
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')