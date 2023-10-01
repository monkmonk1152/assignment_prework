# cooks = ['Tim', 'John', 'Jacob']

# def cooks_add(cooks_to_add):
#     cooks.append(cooks_to_add)

# cooks_add('Chris')
# cooks_add('Ethan')
# cooks_add('Mason')

# print(cooks)

# dogs = ['Neville', 'Chili']

# def dogs_add(dogs_to_add):
#     dogs.append(dogs_to_add)

# dogs_add('Luna')
# dogs_add('Mini')
# dogs_add('Max')

# print(dogs)

# high order fuct.

# def addThree(num):
#     return num + 4

# def addFour(num):
#     return num + 5

# print(addThree(addFour(3)))

# def rafiki(lion):
#     print(lion + " " +
#           "Oh yes, the past can hurt "+
#             "But the way I can see, "+
#                 "you can either run from it or learn from it")
# rafiki("Simba")   

# def dory(fish, minutes_since_last_talked):
#     if minutes_since_last_talked > 10:
#         print("Who are you?", end=" ")
#     else:
#         if fish == "Nemo":
#             print("Just keep swimming", end=" ")
#         else:
#             print("I dont know you", end=" ")
# print(dory("Nemo", 90))
    
# def emperor(word_a, word_b):
#     my_string=("The "+word_b+" that blooms " +
#                "in adversity is the most " +
#                "rare and "+word_a+" of all.")
#     return my_string
# word_1 = 'flower'
# word_2 = 'beautiful'
# print(emperor(word_b=word_1, word_a=word_2))

# def see_character(name, age, species="human"):
#     print(name,age,species)

# see_character("Ariel", 16, "mermaid")

def do_something(a_list):
    my_string=""
    for element in a_list:
        my_string += element[0]
    return my_string
aladdin_characters = ["Jasmine", "Aladdin", "Fazahl", "Abu", "Razoul"]
print(do_something(aladdin_characters))