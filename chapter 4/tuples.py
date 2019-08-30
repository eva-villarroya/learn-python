# immutable list = tuple

dimensions = (200, 50)
print(dimensions[0]) 
print(dimensions[1])

# cannot change values, this fails
#dimensions[0] = 250

for dimension in dimensions:
    print(dimension)


# can change the tuple itself:

dimensions = (400, 100) 
print("\nModified dimensions:")

for dimension in dimensions:
    print(dimension)


foods = ("soup", "spaguetti", "steak", "salad", "ice cream")
print("\nOur menu:")
for food in foods:
    print(food)



