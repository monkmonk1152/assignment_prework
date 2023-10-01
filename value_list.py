requested_toppings = ['mushrooms', 'onions', 'pineapple']
"mushrooms" in requested_toppings
"pepperoni" in requested_toppings
# At u and v, the keyword in tells Python to check for the existence of
# 'mushrooms' and 'pepperoni' in the list requested_toppings. This technique is
# quite powerful because you can create a list of essential values, and then
# easily check whether the value you’re testing matches one of the values in
# the list.


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish")
    # The line at u reads quite clearly. If the value of user is not in the list
# banned_users, Python returns True and executes the indented line.
# The user 'marie' is not in the list banned_users, so she sees a message
# inviting her to post a response.

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
# 5.1 practice pg.82