# 9.3 users
class Users:
    def __init__(self,firstname,lastname):
        self.name = firstname
        self.family = lastname
    
    def describe_user(self):
        return f"{self.name} - {self.family}"
    
    def greet_user(self):
        return f"hello {self.name} you're welcome nice to meet you."

# user1 = Users("mahdieh","mohamadi")
# user2 = Users("leila","mohamadi")
# user3 = Users("kimi","jaladat")
# print(user1.greet_user())
# print(user2.greet_user())
# print(user3.greet_user())

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
    
# user1 = Users('mahdieh','mohammadi')
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.reset_login_attempts()
# print(user1.login_attempts)
