# 5.1 Conditional test
car = "subaru"
if car == "subaru":
    print("car is subaru I predict True")
    
car = "MWM"
if car.lower() == 'mwm':
    print("car is mwm I predict true")

age = 20 
grade = 18
if age > 21 and grade == 19:
    print("age and grade greater then 18. I predict False")

if (age >= 15) | (grade > 19):
    print(f"age is greater than 15 and grade less 19 I predict is true")
    
if (age >= 20) and (grade >= 17):
    print(f"age is {age} and grade is {grade} I predict is true")
    
favorite_food = ['chicken','pizza','peperoni']
if 'chicken' not in favorite_food:
    print("chicken I predict is false")
if "pasta" not in favorite_food:
    print('pasta not in favorite_food I predict true')

city = "Yazd"
if city.lower() == "tehran":
    print("city Tehran I predict false")
    
grade = 12
if grade != 12:
    print("grade not equal 12 I predict false")
elif grade < 10 :
    print("grade is less of ten I predict false")
    
# 5.3 Alien Colors #1:
alien_color = 'green'
if alien_color == 'green':
    print("the player just earned 5 points")
if alien_color == 'blue':
    print("the players just earned 2 points")

# 5.4 Alien Colors #2:
if alien_color == 'green':
    print("the player earned 5 points")
else:
    print("the player earned 10 points")
# 5.5 Alien Colors #3:
alien_color = 'red'
if alien_color == 'green':
    print("the player earned 5 pints")
elif alien_color == 'yellow':
    print("the player earned 10 pints")
elif alien_color == 'red':
    print("the player earned 15 pints")

5.6 stages of life:
age = 33
if age < 2:
    print("the person is baby")
elif age < 4:
    print("the person is toddle")
elif age < 13:
    print("the person is kid")
elif age < 20:
    print("the person is teenager")
elif age < 65:
    print("the person is adult")
else:
    print("the person is old")

# 5.7 Favorite Fruit
favorite_Fruits = ['bananas','pineapple','fig','cherry']
for fruit in favorite_Fruits:
    print(fruit)
print()
if 'bananas' in favorite_Fruits:
    print("you really like bananas")
if 'apple' in favorite_Fruits:
    print("you really like apple")
if "cherry" in favorite_Fruits:
    print("you really like cherry")

# 5.8 Hello Admin and 5.9 No users
userNames = ['mahdieh','admin','kimia','elena']
# userNames = []
if userNames:
    for user in userNames:
        if user == 'admin':
            print(f"wellcome {user} would you like to see status report?")
        else:
            print(f"Hello {user} thank you for loggin again")
else:
    print("Wee need to find some users")

# 5.10 Checking UserNames 
current_user = ['Leila','mahdieh','Kimi','taha']
new_users = ['elena','leila','narges','mahdieh']

current_user = list(map(str.lower,current_user))
if new_users:
    for user in new_users:
        if user in current_user:
            print("the person need to enter with new user")
        else:
            print("user is available")
else:
    print("unfortunatly user for check")

# 5.11 Ordinal Number
ordinal_Numbers = ["1st","2nd","3rd",'4th',"5th","6th","7th","8th","9th"]
for number in ordinal_Numbers:
    if number == "1st":
        print(f"end of {number} is st ")
    elif number == "2nd":
        print(f"end of {number} is nd ")
    elif number == "3rd":
        print(f"end of {number} is rd ")
    else:
        print(number)
