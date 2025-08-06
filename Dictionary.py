# 6.1 Persons
Person = {
    "First_Name" : "Mahdieh",
    "Last_Name" : "Mohammadi",
    "City" : "Yazd"
}
print(Person)

# 6.2 Favorites Numbers:
Favorites_Numbers = {}
i = 0
while i < 5:
    name = input()
    number = int(input())
    Favorites_Numbers[name] = number
    i += 1
print(Favorites_Numbers)

# 6.3 Glossary and 6.4:
Glossary = {
    "pop_List" : "remove an item from any position in list",
    "remove_list" : "this method removing element from a list with a value",
    "del_List" : "removing Element with give position",
    "add_List" : "adding element to a list",
    "len_list" : "show len of list"   
}
for key,value in Glossary.items():
    print(f"{key}:\n\t{value}")
    print()

# 6.5 Rivers 
rivers = {
    'nile': "egypt",
    'Yangtze': "china",
    'anube': "Germany" ,
    'Amazon': "Brazil"
}
for river,country in rivers.items():
    print(f"{river}:\n\t run through {country} \n")
for river in sorted(rivers,reverse=True):
    print(river.title())
print()
for country in sorted(rivers.values(),reverse=True):
    print(country.title())

# 6.6 Polling
favorite_language = {
    "jon" : "python",
    "mehdi" : "c++" ,
    "kimi" : "python",
    "mahdieh" :"all language and python ++"
}
people_poll = ["tina","kimi","mahla","mahdieh"]

for name in favorite_language:
    if name in people_poll:
        print(f"{name} thanking them for responding")
    else:
        print(f"{name} inviting them to take the poll")

# 6.7 people 
Person1 = {
    "First_Name" : "Mahdieh",
    "Last_Name" : "Mohammadi",
    "City" : "Yazd"
}

Person2 = {
    "First_Name" : "kimia",
    "Last_Name" : "Jaladat",
    "City" : "Yazd"
}

Person3 = {
    "First_Name" : "elnaz",
    "Last_Name" : "arjmand",
    "City" : "tehran"
}

persons = [Person1,Person2,Person3]
for person in persons:
    print(person)

# 6.8 pets
pet1 = {
    "animal":"cat",
    "owners":"jack"
}

pet2 = {
    "animal":"bird",
    "owners":"Bob"
}

pet3 = {
    "animal":"fishes",
    "owners":"Alice"
}

animals = [pet1,pet2,pet3]
for animal in animals:
    print(f"{animal['animal']} {animal['owners']}")

# 6.9 Favorite places 
Favorite_places = {
    'leila' : ['Tehran','italy'],
    'kimia' : ['German','landon'],
    'mahdieh' : ['netherland','Austria','Poland']
}
for name,places in Favorite_places.items():
    print(f"{name}:")
    for place in places:
        print(f"\t{place}")
    print()

# 6.10 Favorite Numbers
Favorites_Numbers = {}
i = 0
while i < 5:
    name = input()
    number = list(map(int,input().split()))
    Favorites_Numbers[name] = number
    i += 1

for name,numbers in Favorites_Numbers.items():
    print(f"{name} your favorite places are:")
    for number in numbers:
        print(f"\t{number}")
    print()

# 6.11 cities 
cities = {
    'Tehran': {
        'info' : "It's the capital in Iran",
        'country': 'Iran'
        
    },
    'Berlin': {
        'info' : "Berlin is a global city of culture, politics, media and science.",
        'country': 'Germany'
        
    },
    'Amsterdam':{
        'info' : "It's the capital and most populous city in the country",
        'country': 'Netherland'      
    }}

for city,information in cities.items():
    print(city)
    print(f"{information['info']} \t Country is: {information['country']}")