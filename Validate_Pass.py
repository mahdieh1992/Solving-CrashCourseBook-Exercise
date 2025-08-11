def validate_password(password):
    if len(password) < 8:
        print("password must be at least 8 character")
    elif password.isnumeric():
        print("password should have at least 1 letter")
    elif password.isalpha():
        print("password should have at least 1 number")
    else:
        print("password is verify")
valid = True
while valid:
    password = input("please enter new password:")
    validate_password(password)
