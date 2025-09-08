# 9.1 Restaurant 
class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        
    def describe_restaurant(self):
        return f"{self.name} is a type of {self.type} restaurant"

    def open_restaurant(self):
        return f"{self.name} is open"

# Restaurant1 = Restaurant('ras','traditional')
# print(Restaurant1.describe_restaurant())
# print(Restaurant1.open_restaurant())

# 9.2 three Restaurant

Restaurant1 = Restaurant('ras','traditional')
Restaurant2 = Restaurant('emarat','traditional')
Restaurant3 = Restaurant('ali','fastFood')
print(Restaurant1.describe_restaurant())
print(Restaurant2.describe_restaurant())
print(Restaurant3.describe_restaurant())


# 9.3 users
class Users:
    def __init__(self,firstname,lastname):
        self.name = firstname
        self.family = lastname
    
    def describe_user(self):
        return f"{self.name} - {self.family}"
    
    def greet_user(self):
        return f"hello {self.name} you're welcome nice to meet you."

user1 = Users("mahdieh","mohamadi")
user2 = Users("leila","mohamadi")
user3 = Users("kimi","jaladat")
print(user1.greet_user())
print(user2.greet_user())
print(user3.greet_user())

# 9.4 Number Served
class Restaurant:
    """ describe a restaurant"""
    def __init__(self,name,type):
        """ initialize attributes for a restaurant """
        self.name = name
        self.type = type
        self.number_Served = 0
        
    def set_number_served(self,numberServe):
        self.number_Served = numberServe
        
    def increment_number_served(self,numberServe):
        self.number_Served += numberServe

restaurant1 = Restaurant('Emarat','Fancy')   
# print(restaurant1.number_Served)  
# restaurant1.number_Served = 500
restaurant1.set_number_served(200)
restaurant1.set_number_served(100)
restaurant1.increment_number_served(200)
restaurant1.increment_number_served(30)
print(restaurant1.number_Served)

# 9.5 Login attempt
class Users:
    """ a simple attempt to represent login users"""
    def __init__(self,firstname,lastname):
        self.name = firstname
        self.family = lastname
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
user1 = Users('mahdieh','mohammadi')
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

# 9.6 Ice Cream Stand
class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)
        self.flavors = ['orange','berry','pineapple','banana']
        
    def describe_flavor(self):
        if self.flavors:
            for flavor in self.flavors:
                print(flavor)
                
                
ice1 = IceCreamStand('paliz','classic')
ice1.describe_flavor()

# 9.8 privileges
class Privileges:
    def __init__(self):
        self.privileges = ['can delete post','can add post','can ban user']
        
    def show_privileges(self):
        if self.privileges:
            for privilege in self.privileges:
                print(privilege)

# 9.7 Admin
class Admin(Users):
    def __init__(self,firstname,lastname):
        super().__init__(firstname,lastname)
        self.privilege = Privileges()
               
admin1 = Admin('mahdieh','mohamadi')
admin1.privilege.show_privileges()

# 9.9 Battery Upgrade 
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

class Battery:
    def __init__(self,size = 40):
        self.size = size
    
    def describe_battery(self):
        print(f"battery size is {self.size}")
        
    def get_range(self):
        range = 0
        if self.size == 40:
            range = 150
        elif self.size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        if self.size == 40:
            self.size = 65
        
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.batterySize = Battery()
    

car1 = ElectricCar('iran','mvm',2019)
car1.batterySize.describe_battery()
car1.batterySize.get_range()
car1.batterySize.upgrade_battery()
car1.batterySize.get_range()

    


