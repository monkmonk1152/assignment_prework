# while True:
#     my_pet = input("What is your pet?\n")
#     if my_pet.lower() == 'quit':
#         break
#     elif my_pet.lower()[0] in 'dog':
#         print('Go to room one please')
#     elif my_pet.lower()[0] in 'cat':
#         print('Please go to room two')
#     elif my_pet.lower()[0] in 'rabbit':
#         print('please go to room three')

def greet_user(user_name):
    """Display a simple greeting"""
    print('Hello! ' +  user_name.title() + ', lets get started!')
greet_user('jessie')
# """  """ is a docstring
