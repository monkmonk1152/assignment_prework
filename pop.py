motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)
# line 2-4 shows how to use the pop() action which removes the last element in the list
# line 5 uses pop() to show you still have access to the element pop()

motorcycles = ['honda', 'yamaha', 'suzuki']
# last_owned = motorcycles.pop()
# print("The last motorcycle I owned was a " + last_owned.title() + ".")
# this shows putting the action into last_owened and pops the last item into in str

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# first_owned = motorcycles.pop(0)
# print("The first motorcycle I owned was a " + first_owned.title() + ".")
# this uses the pop() to take the spot named on the list and adds it to the str

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")