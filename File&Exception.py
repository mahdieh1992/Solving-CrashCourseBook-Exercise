# 10.1 Learning python & 10.2 Learning C & 10.3 simpler code
from pathlib import Path
file1 = Path("./CrashCourse/Learning_Python.txt").read_text()
for line in file1.splitlines():
    print(line.replace("python","c#"))

# 10.4 Guest & 10.5 Guest Book
from pathlib import Path
list_names = ""
for i in range(5):
    get_Name = input("Enter your Name please:")
    list_names += f"{get_Name}\n"
    
path_file = Path("./CrashCourse/guest_books.txt")   
path_file.write_text(list_names)
print(path_file.read_text())
    
# 10.6 Addition # 10.7 addition calculate
while True:
    a = input("Enter num: ")  
    if a == 'q':
        break
    b = input("Enter num: ") 
    if b == 'q':
        break
    try:
        a = int(a)
        b = int(b) 
    except ValueError:
        print("type of value is not correct")
    else:
        print(a + b)

# 10.8 cats and dogs # 10.9 silent cats and dogs
from pathlib import Path

def readFiles(path):
    try:
        path.read_text()
    except FileNotFoundError:
        print("sorry file is not exists")
    else:
        print(path.read_text())  

file1 = Path("./CrashCourse/Cat1s.txt")
readFiles(file1)

# 10.10 common words 
from pathlib import Path
path =  Path("./CrashCourse/Cats.txt")
fileRead = path.read_text()
print(fileRead.count("o"))

# 10.11 Favorite number
from pathlib import Path
import json

favoriteNumbers = []
while True:
    num = input()
    if num == 'q':
        break
    try:
        int(num)
    except ValueError:
        print("it is not number")
    else:
        favoriteNumbers.append(int(num))

pathFile = Path("./CrashCourse/number.json")
pathFile.write_text(json.dumps(favoriteNumbers))


path = Path("./CrashCourse/number.json")
content = path.read_text()
print(json.loads(content))


# 10.11 Favorite number Remembered

from pathlib import Path
import json

favoriteNumbers = []
def favorite_number():
    # get numbers and store in json file and read of json file
    pathFile = Path("./CrashCourse/number.json")
    if pathFile.exists():
        content = pathFile.read_text()
        print(json.loads(content))
    else:
        while True:
            num = input()
            if num == 'q':
                break
            try:
                int(num)
            except ValueError:
                print("it is not number")
            else:
                favoriteNumbers.append(int(num))
        pathFile.write_text(json.dumps(favoriteNumbers))
favorite_number()

# 10.13 User Dictionary 10.14

from pathlib import Path
import json
class User:
    def __init__(self,path,userName,lastName,Email,isLogin):
        self.path = path
        self.userName = userName
        self.lastName = lastName
        self.Email = Email
        self.isLogin = isLogin
        
    def createUser(self):
        # prompt for a new user
        self.path.write_text(json.dumps({
            "name":self.userName,
            "lastName":self.lastName,
            "Email":self.Email,
            "isLogin": self.isLogin
        }))
    
    def show_user(self):
        # show users that created
        pathFile = self.path
        if self.path.exists():
            return json.loads(pathFile.read_text())
        else:
            self.createUser()
            return json.loads(pathFile.read_text())
    
    def greet_user(self):
        # greeting if user exists 
        users = self.show_user()
        if users:
            return f"welcome {users['name'] } ** {users['lastName']}"
                
path = Path("./CrashCourse/usersInfo.json")
user2 = User(path,'mina','mohamadi','mina@gmail.com',False)
print(user2.greet_user())