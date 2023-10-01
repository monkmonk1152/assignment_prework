pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'cheese', 'black olives']
}
print("You ordered a " + pizza['crust'] + "-crust pizza " +
 "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

#     We begin at u with a dictionary that holds information about a pizza
# that has been ordered. One key in the dictionary is 'crust', and the associated value is the string 'thick'. The next key, 'toppings', has a list as its value
# that stores all requested toppings. At v we summarize the order before
# building the pizza. To print the toppings, we write a for loop w. To access
# the list of toppings, we use the key 'toppings', and Python grabs the list of
# toppings from the dictionary.