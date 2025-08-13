def fullName(firstName,lastName,*args):
    get_fullName = {'firsName':firstName,'lastName':lastName,'other':args}
    return f"Hello {get_fullName['firsName']} {get_fullName['lastName']} {get_fullName['other']}"

while True:
    print("Please tell me your name and lastName and everything")
    print("if you want to quit please enter q")
    firstName = input("Please enter yourName: ")
    if firstName == 'q':
        break
    lastName = input("Please enter lastName: ")
    if lastName == 'q':
        break
    other = input("Please enter your additional info:")
    if other == 'q':
        break
    else:
        print(fullName(firstName,lastName,other))