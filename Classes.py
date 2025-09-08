from Restaurant import Restaurant
from User import Users
# 9.6 Ice Cream Stand
class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)
        self.flavors = ['orange','berry','pineapple','banana']
        
    def describe_flavor(self):
        if self.flavors:
            for flavor in self.flavors:
                print(flavor)
                
                
# ice1 = IceCreamStand('paliz','classic')
# ice1.describe_flavor()

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
               
# admin1 = Admin('mahdieh','mohamadi')
# admin1.privilege.show_privileges()

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
    

# car1 = ElectricCar('iran','mvm',2019)
# car1.batterySize.describe_battery()
# car1.batterySize.get_range()
# car1.batterySize.upgrade_battery()
# car1.batterySize.get_range()

# 9.10 Imported Restaurant
restaurant1 = Restaurant('emarat','fancy')
print(restaurant1.name)

    


