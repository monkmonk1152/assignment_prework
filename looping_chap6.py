# user_0 = {
#  'username': 'efermi',
#  'first': 'enrico',
#  'last': 'fermi',
#  }
# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)

#     As shown at 1, to write a for loop for a dictionary, you create names for
# the two variables that will hold the key and value in each key-value pair. You
# can choose any names you want for these two variables. This code would work
# just as well if you had used abbreviations for the variable names, like this:
# for k, v in user_0.items()
# The second half of the for statement at 2 includes the name of the dictionary followed by the method items(), which returns a list of key-value pairs.
# The for loop then stores each of these pairs in the two variables provided.
# In the preceding example, we use the variables to print each key v, followed
# by the associated value 3. The "\n" in the first print statement ensures that a
# blank line is inserted before each key-value pair in the output:

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
# for name in favorite_languages.keys():
    # print(name.title())
    # this pulls the keys which in this case is the names
    # the action .keys() is used
# Looping through the keys is actually the default behavior when looping
# through a dictionary, so this code would have exactly the same output if you
# wrote . . .
# for name in favorite_languages:
# rather than . . .
# for name in favorite_languages.keys():

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + 
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")
# Sarah
#  Hi Sarah, I see your favorite language is C!
# Edward
# Phil
#  Hi Phil, I see your favorite language is Python!
# This is the outcome of this code

print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title())
#  The for statement here pulls each value from the dictionary


