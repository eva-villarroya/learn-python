answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19

print("Age is " + str(age))

print("Is age under 21?")
print(age < 21)
print("Is age under or equal to 21?")
print(age <= 21)
print("Is age above 21?")
print(age > 21)
print("Is age above or equal to 21?")
print(age >= 21)
print("Is age equal to 21?")
print(age == 21)

age_0 = 22
age_1 = 18

print("Ages are " + str(age_0) + ", "+ str(age_1))

print("Are both ages above 21?")
print(age_0 >= 21 and age_1 >= 21)

print("Is any age above 21?")
print(age_0 >= 21 or age_1 >= 21)


requested_toppings = ['mushrooms', 'onions', 'pineapple']
print("Toppings are " + str(requested_toppings))
print("Is mushrooms a topping?")
print('mushrooms' in requested_toppings)
print("Is pepperoni a topping?")
print('pepperoni' in requested_toppings)


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
