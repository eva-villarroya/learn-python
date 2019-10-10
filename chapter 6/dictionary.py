person = {'surname': 'Dough', 'name': 'John'}

print("\nA dictionary: ")
print(person)

print("\nAdding a new key/value")
person['age'] = 56
print(person)

print("\nSubstitutes a value for a key")
person['surname'] = 'Doe'
print(person)

print("\nRemoves a key/value")
del person['age']
print(person)

print("\nLoops key/values")
for key, value in person.items():
    print("Key: " + key)
    print("Value: " + value)

print("\nLoops keys only by default")
for key in person:
    print("Key: " + key)

print("\nLoops values only")
for value in person.values():
    print("Value: " + value)

print("\nLoops the sorted keys")
for key in sorted(person.keys()):
    print(key.title())

print("\nLoops the sorted values, removes duplicates")

favorite_languages = { 'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', }

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
