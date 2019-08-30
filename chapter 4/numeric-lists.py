for value in range(1,5):
    print(value)


print("\n")

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)


# indentitation must be exact in amount and type (no mix of tabs and spaces)
squares = []

for value in range(1,11): 
    square = value**2
    squares.append(square)

print(squares)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


# list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

# print numbers 1-20
[print(value) for value in range(1,21)]

million = []

# make a list of million items, print them. Not using for to print as this way is faster
[million.append(value) for value in range(1,1000001)]
#print(million)

# and now I can print the sum

print(sum(million))


odd_numbers = list(range(1,21,2))
print(odd_numbers)

three_multiples = list(range(3,31,3))
print(three_multiples)

first_ten = list(range(1,11))
print([value**3 for value in first_ten])

# comprehension brackets dont seem mandatory if is function param?
# see explanation below
test = list(value**3 for value in first_ten)
[print(value) for value in test]


comprehension = [value+1 for value in first_ten]
generator = (value+1 for value in first_ten)

print(comprehension)
# generator is of type Generator, need to convert to list to print it
print(list(generator))
print("Again")
print(comprehension)
# generator is exhausted, as explained here
# https://stackoverflow.com/questions/10998521/square-braces-not-required-in-list-comprehensions-when-used-in-a-function
print(list(generator))
