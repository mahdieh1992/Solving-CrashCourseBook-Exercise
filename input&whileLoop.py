# # 7.1 rental car
# message = input("what kind of rental car would you like?")
# print(f"let me see if I can find you a{message}")

# # 7.2 Restaurant Seating
# count_people = int(input("How many people are in their dinner group?\n"))
# if count_people > 8:
#     print("they'll have to wait for a table")
# else:
#     print("that their table is ready")

# # 7.3 Multiple of Ten 
# number = int(input("please Enter a number"))
# if number % 10 == 0:
#     print(f"{number} is multiple of 10")
# else:
#     print(f"{number} is not multiple of 10")
    
# # 7.4 Pizza Toppings
# while True:
#     topping = input()
#     if topping != "quit":
#         print(f"{topping} is added your pizza")
#     else:
#         break

# # 7.5 Movie tickets
# i = 0
# while i < 5:
#     i += 1
#     user_age = int(input())
#     if user_age < 3:
#         print("your ticket is free")
#     elif user_age < 12:
#         print("your ticket is 10$")
#     elif user_age > 12:
#         print("your ticket is 15$")
    
# # 7.6 Three exits
# i = 0
# while i < 5:
#     i += 1
#     user_age = input()
#     if user_age == 'quit' :
#         break
#     user_age = int(user_age)
#     if user_age < 3:
#         print("your ticket is free")
#     elif user_age < 12:
#         print("your ticket is 10$")
#     elif user_age > 12:
#         print("your ticket is 15$")

# # 7.6 three exits
# active = True
# while active:
#     user_age = input()
#     if user_age == 'quit' :
#         active = False
#     else:
#         user_age = int(user_age)
#         if user_age < 3:
#             print("your ticket is free")
#         elif user_age < 12:
#             print("your ticket is 10$")
#         elif user_age > 12:
#             print("your ticket is 15$")
    
# # 7.7 Infinity
# i = 1
# while i < 3:
#     print(i)

# # 7-8 Deli:
# sandwich_orders = ['Bacon','Pastrami','egg and cheese','Pastrami','Bagel toast','Pastrami','Beef on weck']
# finished_sandwiches = []
# while sandwich_orders:
#     made_sandwich = sandwich_orders.pop(0)
#     print(f"I'm making your {made_sandwich} sandwich")
#     finished_sandwiches.append(made_sandwich)
# for sandwich in finished_sandwiches:
#     print(f"your {sandwich} is prepare")

# # 7.9 No Pastrami
# sandwich_orders = ['Bacon','Pastrami','egg and cheese','Pastrami','Bagel toast','Pastrami','Beef on weck']
# while 'Pastrami' in sandwich_orders:
#     sandwich_orders.remove('Pastrami')
# print(sandwich_orders)

# 7.10 Dram vacation
polling_active = True
favorite_vacation = {}
while polling_active:
    name = input("\n what's your name?")
    response = input("if you could visit one place in the world where do you go?")
    favorite_vacation[name] = response
    repeat = input("would you like keeping poll?")
    if repeat == 'no':
        polling_active = False
        
for name,response in favorite_vacation.items():
    print(f"{name} your favorite vacation is {response}")