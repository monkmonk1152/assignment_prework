favorite_languages = {
    'jen' :['python', 'ruby'],
    'sarah':['c'],
    'edward':['ruby', 'go'],
    'phil':['python', 'haskill'],
}

for name, languages in favorite_languages.items():
 print("\n" + name.title() + "'s favorite languages are:")
 for language in languages:
  print("\t" + language.title())

#   As you can see at 1 the value associated with each name is now a list.
# Notice that some people have one favorite language and others have
# multiple favorites. When we loop through the dictionary at 2, we use the
# variable name languages to hold each value from the dictionary, because we
# know that each value will be a list. Inside the main dictionary loop, we use
# favorite_
# languages.py
# Dictionaries 113
# another for loop 3 to run through each person’s list of favorite languages.
# Now each person can list as many favorite languages as they like