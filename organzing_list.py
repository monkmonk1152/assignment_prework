cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# this puts list in alphabetical order permanently

# cars.sort(reverse=True)
# print(cars)
# this action does the same as above just in reverse

# print("Here is the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print("\nHere is the original list again:")
# print(cars)
# We first print the list in its original order at 1 and then in alphabetical
# order at 2. After the list is displayed in the new order, we show that the list is
# still stored in its original order at 3.

# printing list using the reverse fuction
cars.reverse()
print(cars)
# Notice that reverse() doesn’t sort backward alphabetically; it simply
# reverses the order of the list: