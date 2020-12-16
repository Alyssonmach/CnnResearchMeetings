favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python' }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.capitalize())

print("\nThe following names have been mentioned:")
for names in favorite_languages.keys():
    print(names.capitalize())