# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
# # The dictionary alien_0 stores the alien’s color and point value. The two
# # print statements access and display that information, as shown here:

# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points!")
# # \Once the dictionary has been defined, the code at u pulls the value
# # associated with the key 'points' from the dictionary. This value is then
# # stored in the variable new_points. The line at v converts this integer value
# # to a string and prints a statement about how many points the player just
# # earned

# # position of the alien
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# # starting with a empty dictionary
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# # adding or append to empty list


# # alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# # print("Original x-position: " + str(alien_0['x_position']))
# # alien_0 = {'color': 'green'}
# # print("The alien is " + alien_0['color'] + ".")
# # alien_0['color'] = 'yellow'
# # print("The alien is now " + alien_0['color'] + ".")
# # if alien_0['speed'] == 'slow':
# #   x_increment = 1
# # elif alien_0['speed'] == 'medium':
# #   x_increment = 2
# # else:
# #   x_increment = 3
# #   print("New x-position: " + str(alien_0['x_position']))

# # removing key value pairs

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

# # The line at u tells Python to delete the key 'points' from the dictionary
# # alien_0 and to remove the value associated with that key as well. The output
# # shows that the key 'points' and its value of 5 are deleted from the dictionary, but the rest of the dictionary is unaffected:

# # similar objects

# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',}
# print("Sarah's favorite language is " +
#       favorite_languages['sarah'].title() +
#       ".")

user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value:" + value)