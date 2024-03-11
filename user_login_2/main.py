sys_username = "furkan"
sys_password = "1234"

rightof_entry = 3

while True:
    username = input("Username: ")
    password = input("Password: ")

    if (username != sys_username and password == sys_password):
        print("Incorrect Username!")
    elif (username == sys_username and password != sys_password):
        print("Incorrect Password!")
        rightof_entry -=1
    elif(username != sys_username and password != sys_password):
        print("Incorrect Username and Password!")
        rightof_entry -= 1
    else:
        print("Welcome!")
        break
    if (rightof_entry == 0):
        print("You no longer have access rights. Please try again later.")
        break
