# # 9.1 Restaurant 
# class Restaurant:
#     def __init__(self,name,type):
#         self.name = name
#         self.type = type
        
#     def describe_restaurant(self):
#         return f"{self.name} is a type of {self.type} restaurant"

#     def open_restaurant(self):
#         return f"{self.name} is open"

# # Restaurant1 = Restaurant('ras','traditional')
# # print(Restaurant1.describe_restaurant())
# # print(Restaurant1.open_restaurant())

# # 9.2 three Restaurant

# Restaurant1 = Restaurant('ras','traditional')
# Restaurant2 = Restaurant('emarat','traditional')
# Restaurant3 = Restaurant('ali','fastFood')
# print(Restaurant1.describe_restaurant())
# print(Restaurant2.describe_restaurant())
# print(Restaurant3.describe_restaurant())
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

# restaurant1 = Restaurant('Emarat','Fancy')   
# # print(restaurant1.number_Served)  
# # restaurant1.number_Served = 500
# restaurant1.set_number_served(200)
# restaurant1.set_number_served(100)
# restaurant1.increment_number_served(200)
# restaurant1.increment_number_served(30)
# print(restaurant1.number_Served)
