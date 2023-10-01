players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# this action takes the 1st 3 names from list

# print(players[1:4])
# this pulls 2 3 4 from list

# print(players[:4])
# this action will make python start from the 1st item till the last one you list

# print(players[2:])
# This syntax allows you to output all of the elements from any point in
# your list to the end regardless of the length of the list. Recall that a negative index returns an element a certain distance from the end of a list;
# therefore, you can output any slice from the end of a list

# print(players[-3:])
# This prints the names of the last three players and would continue to
# work as the list of players changes in size.

print("Here are the first three players on my team:")
for player in players[:3]:
 print(player.title())
#  ref. pg.66

my_list = ["apple", "banana", "orange", "berries", "corn"]
print(f'my favorite food is {my_list[2]} and also {my_list[3]}')
# print(my_list[2::2])
# start End Step
# print(f) puts python code back into python
