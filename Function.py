# 8.1 Message
def display_message():
    print("I'm learning about Functions")
# display_message()

# 8.2 Favorite book
def favorite_book(title):
    print(f"my favorite book is {title}")
favorite_book("python")

# 8.3 T-Shirt
def make_shirt(size):
    print(f"size shirt is {size}")

make_shirt("xl")
make_shirt(size="L")

# 8.4 Large Shirts
def make_shirt(size = "Large",message = "I love python"):
    print(f"size shirt is {size},{message}")
make_shirt("medium")
make_shirt()
make_shirt("small","I love this shirts")

# 8.5 cities
def describe_city(city,country="iran"):
    print(f"{city} is in {country}")
    
describe_city("Tehran")
describe_city("Berlin","Germany")
describe_city("Yazd")

# 8.6 city Names
def city_country(city,country):
    city_country = f"{city}, {country}"
    return city_country

i = 0
while i < 3:
    city = input("please Enter city:")
    country = input("please Enter country:")
    print(city_country(city,country))
    i += 1

# 8.7 album
def make_Album (artistName,album,numberSong='None'):
    info_artist = {'artistName':artistName, 'album':album, 'numbersOfSong':numberSong}
    return f"{info_artist['artistName']}: \n\t {info_artist['album']}\t {info_artist['numbersOfSong']}"


while True:
    artistName = input("Please Enter artist's name: ")
    album = input(f"Please Enter album {artistName}: ")
    numberOfSongs = input(f"Please Enter artist's {artistName}: ")
    print(make_Album(artistName,album,numberOfSongs))
    quit = input("would you like to exits? Please enter yes else no:\n")
    if quit == 'yes':
        break

# 8.9 Messages 
def show_message(messages):
    for message in messages:
        print(message)
list_Message = ['blue','yellow','pink','red','green']
show_message(list_Message)

# 8.10 Sending Messages
def send_messages(messages):
         while messages:
           current_message = messages.pop()
           print(current_message)
           sent_Message.append(current_message)

list_Message = ['blue','yellow','pink','red','green']
sent_Message = []
send_messages(list_Message)
print(list_Message,sent_Message)


# 8.11 Archived Messages
send_messages(list_Message[:])
print(list_Message,sent_Message)


# 8.12 SandWiches
def make_Sandwiches(*items):
    for item in items:
        print(item)

make_Sandwiches("cheese","mushroom","pepper","onion")
print()
make_Sandwiches("cheese","mushroom")

# 8.13 userProfile
def build_Profile(first,last,**userInfo):
    userInfo['firstName'] = first
    userInfo['lastName'] = last
    return userInfo

print(build_Profile('mahdieh','mohammadi',city = 'yazd' , language = 'persion' , occupation = 'engineer'))

# 18.4 Cars
def make_car(manufacturer,model_Name,**info_Car):
    info_Car['manufacturer'] = manufacturer
    info_Car['model'] = model_Name
    return info_Car

car = make_car('subaru','outback',color = 'blue' ,tow_package = True)
print(car)
    
# 8.15 printing models
from printing_models import * # make_pizza as mp 
make_pizza(2,'mushrooms','pepper','cheeses')