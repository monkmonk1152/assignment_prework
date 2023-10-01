# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])
# this shows the the dimensions of a box, this will make sure it dont change

# dimensions = (200, 50)
# dimensions[0] = 250
# this does not work, python cant run it

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
 print(dimension)
 dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)
#  this is how to modified the dimensions