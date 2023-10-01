# def greet_users(names):
#  """Print a simple greeting to each user in the list."""
#  for name in names:
#    msg = "Hello, " + name.title() + "!"
#    print(msg)
#  usernames = ['tim','anna','jacob','john','shawn','tyson']
# greet_users(usernames)

# mod a list in a function
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# while unprinted_designs:
#  current_design = unprinted_designs.pop()
 
#  print("Printing model: " + current_design)
#  completed_models.append(current_design)

#  print("\nThe following models have been printed:")
# for completed_model in completed_models:
#  print(completed_model)


# using 2 fuctions

# def print_models(unprinted_designs, completed_models):
#   """Simulate printing each design, until none are left.
#  Move each design to completed_models after printing."""
#   while unprinted_designs:
#    current_design = unprinted_designs.pop()
#    print("Printing model: " + current_design)
#   completed_models.append(current_design)


# def show_completed_models(completed_models):
#   """Show all the models that were printed."""
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# Passing an Arbitrary Number of Arguments

# def make_pizza(*toppings):
#   """Summarize the pizza we are about to make."""
#   print("\nMaking a pizza with the following toppings:")
#   for topping in toppings:
#    print("- " + topping)


# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Mixing Positional and Arbitrary Arguments

# def make_pizza(size, *toppings):
#  """Summarize the pizza we are about to make."""
#  print("\nMaking a " + str(size) +
#  "-inch pizza with the following toppings:")
#  for topping in toppings:
#   print("- " + topping)

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using Arbitrary Keyword Arguments

# def build_profile(first, last, **user_info):
#  """Build a dictionary containing everything we know about a user."""
#  profile = {}
#  profile['first_name'] = first
#  profile['last_name'] = last
#  for key, value in user_info.items():
#   profile[key] = value
#  return profile
# user_profile = build_profile('albert', 'einstein',
#  location='princeton',
#  field='physics')
# print(user_profile)


# Importing an Entire Module

