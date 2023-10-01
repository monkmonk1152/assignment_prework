# def greet_users():
#     """display a greeting"""
#     print('Hello, ' + "everyone"  + " welcome to the party.")
# greet_users()


# def guest():
#     """display a greeting"""
#     print("Hello, " + "hope all is well," +" Lets get this going!")
# guest()

# def describe_pet(animal_type, pet_name):
#    """Display information about a pet."""
#    print("\nI have a " + animal_type + ".")
#    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('dog', 'neville') 

# The definition shows that this function needs a type of animal and the
# animal’s name u. When we call describe_pet(), we need to provide an animal type and a name, in that order. For example, in the function call, the
# argument 'hamster' is stored in the parameter animal_type and the argument 'harry' is stored in the parameter pet_name v. In the function body,
# these two parameters are used to display information about the pet being
# described.

# def describe_cities(cities_size, cities_location):
#     """Display cities information about cities"""
#     print("\n Atlanta is in "  + cities_location + ".")
#     print("Atlanta is a " + cities_size + " city!")
# describe_cities(cities_size='large', cities_location='Georgia')

# def make_shirt(shirt_size, shirt_logo="UGA, Bama, Go Vols "):
#     """display shirt information"""
#     print("\n we have three shirt sizes " + shirt_size + ".")
#     print(" we have shirts with sayings like " + shirt_logo +"!")
# make_shirt(shirt_size='XL, XXL, LG, Med, SL')


# def get_formatted_name(first_name, last_name):
#     """return full name, neatly formatted"""
#     full_name=first_name + ' ' + last_name
#     return full_name.title()
# cook = get_formatted_name('christopher', 'eason')
# print(cook)

# def get_formatted_name(first_name, middle_name, last_name):
#  """Return a full name, neatly formatted."""
#  full_name = first_name + ' ' + middle_name + ' ' + last_name
#  return full_name.title()

# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)

# returning a dict.
# def build_person(first_name, last_name, age=""):
#  """Return a dictionary of information about a person."""
#  person = {'first': first_name, 'last': last_name}
#  if age:
#     person['age']= age
#  return person

# cook = build_person('Christopher', 'Eason', '30')
# print(cook)

# using a function with a loop
# def get_formatted_name(first_name, last_name):
#  """Return a full name, neatly formatted."""
#  full_name = first_name + ' ' + last_name
#  return full_name.title()
# while True:
#  print("\nPlease tell me your name:")
#  print("(enter 'q' at any time to quit)")

#  f_name = input("First name: ")
#  if f_name == 'q':
#   break

#  l_name = input("Last name: ")
#  if l_name == 'q':
#   break


#  formatted_name = get_formatted_name(f_name, l_name)
#  print("\nHello, " + formatted_name + "!")


# passing a list
def greet_users(names):
 """Print a simple greeting to each user in the list."""
 for name in names:
  msg = "Hello, " + name.title() + "!"
 print(msg)
 usernames = ['tim','anna','jacob','john','shawn','tyson']
 greet_users(usernames)