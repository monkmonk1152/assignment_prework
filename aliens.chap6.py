aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': '10', 'speed':'fast', 'eyes': 'big'}
    aliens.append(new_alien)
for alien in aliens[0:5]:
 print(alien)
print("Total number of aliens: " + str(len(aliens)))

# This example begins with an empty list to hold all of the aliens that
# will be created. At u range() returns a set of numbers, which just tells
# Python how many times we want the loop to repeat. Each time the loop
# runs we create a new alien v and then append each new alien to the list
# aliens w. At x we use a slice to print the first five aliens, and then at y we
# print the length of the list to prove we’ve actually generated the full fleet
# of 30 aliens.
# **run to see results**

#  for alien in aliens[0:30]:
#   if alien['color'] == 'green':
#    alien['color'] = 'yellow'
#    alien['speed'] = 'medium'
#    alien['points'] = 20
# for alien in aliens[0:5]:
#   elif alien['color'] == 'yellow':
#     alien['color'] = 'red'
#     alien['soeed'] = 'very_fast'
#     alien['points'] = 32
#     print(alien['color'])