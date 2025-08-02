# 4.1 Pizzas

Pizzas = ['Chicken','Pepperoni','Special','Itanlian']
for item in Pizzas:
    print(f"I like {item} pizza")
print(f"I really love pizza!")

# 4.2 Animals
animals = ['tiger','bear','wolf']
for animal in animals:
    print(f"{animal} Great hearing and smell.")
print("They often mark and defend their territory.")

# 4.3 Counting to Twenty
for value in range(1,20):
    print(value)

# 4.4 One Million 
new_List = list(range(1,1000000))
for value in new_List:
    print(value)

# 4.5 Summing a million
print(min(new_List))
print(max(new_List))
print(sum(new_List))

# 4.6 Odd Numbers
odd_Numbers = list(range(1,20,2))
for value in odd_Numbers:
    print(value)

# 4.7 threes 
list_threes = []
for value in range(3,30):
    new_Value = value * 3
    list_threes.append(new_Value)
    print(new_Value)

# 4.8 cubes
cubes_Number = []
for value in range(1,10):
   cube_num = value ** 3
   cubes_Number.append(cube_num)
   print(cube_num)

#4.9 cubes comprehension
cubes_number = [value ** 3 for value in range(1,10)]
print(cubes_number)

# 4.10 Slice
Pizzas = ['Chicken','Pepperoni','Special','Itanlian']
print("The first three items is the list are:")
print(f"{Pizzas[:3]}\n")

print("Three items from the middle of the list are:")
middle = len(Pizzas) // 2
print(f"{Pizzas[middle - 1:3]}\n")

print(f"The last three items in the list are:")
print(Pizzas[-3:])

# 4.11 My pizzas, your pizzas
my_Pizza = ['Chicken','Pepperoni','Special','Itanlian']
friend_pizzas = my_Pizza[:]

my_Pizza.append("RostBif")
friend_pizzas.append("vegetable")

print("my favorite pizzas are:")
for pizza in my_Pizza:
    print(pizza)

print()
print(f"My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)