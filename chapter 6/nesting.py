person_1 = {"name": "John", "surname": "Doe"}
person_2 = {"name": "Amanda", "surname": "Right"}
person_3 = {"name": "Janet", "surname": "Doent"}

people = [person_1, person_2, person_3]

print("People:")
for person in people:
    print(person)

print("List in a dictionary:")
pizza = {'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

print("A dictionary inside a dictionary")

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
