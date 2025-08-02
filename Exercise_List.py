# 3.1 Names
names = ['kimia','elena','leila','zohreh']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3.2 Greeting
print(f"my best friend is {names[0]}")
print(f"my best baby sister is {names[1]}")
print(f"my best sister is {names[2]}")
print(f"my best sister is {names[3]}")

# 3.3 Your Own List
transportation = ['car','motorcycle','cycle']
print(f"I would like to own {transportation[0]}")
print(f"I would like to own {transportation[1]}")
print(f"I would like to own {transportation[2]}")

# 3.4 Guest List
invite_dinner = ['kimia','leila','elena','zohreh','shokuh']

# 3.5 Changing Guest List
invite_dinner.remove('leila')
invite_dinner.insert(1,'maryam')

# 3.6 More Guests
invite_dinner.insert(0,'henieh')
invite_dinner.insert(3,'tina')
invite_dinner.append('mobina')

# 3.7 Shrinking Guest List 

print("Sorry I just invite two people for dinner")

while len(invite_dinner) != 2  :
    guest_pop = invite_dinner.pop(0)
    print(f"sorry {guest_pop} you can't invite to dinner")

del invite_dinner[0]
del invite_dinner[0]

print(invite_dinner)

# 3.8 Seeing the world

country = ['Netherlands','Germany','Italy','Türkiye','Dubai','South Korea']
tem_order = sorted(country,reverse=True)
print(tem_order)
tem_order.reverse()
print(tem_order)
country.sort()
print(country)

# 3.9 Dinner Guests
invite_dinner = ['kimia','leila','elena','zohreh','shokuh']
print(len(invite_dinner))

# 3.10 Every Function
favorite_sports = ['swimming','badminton','volleyball','bodybuilding','skate']
favorite_sports.append('dance')
favorite_sports.insert(1,'Trx')
print(favorite_sports[1])
favorite_sports.pop(0)
print(favorite_sports)
del favorite_sports[2]
print(favorite_sports)
favorite_sports.remove('skate')
print(favorite_sports)
favorite_sports.sort(reverse=True)
tmp_favorite = sorted(favorite_sports)
print(tmp_favorite)
print(favorite_sports)

myList = ['ali','maryam','kimi','tina']
for name in myList:
    print(f"{name.title()} that's great your welcome")
    print(f"i can help {name.title()} \n")
