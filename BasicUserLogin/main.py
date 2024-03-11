sys_username = "beginner"
sys_password = "123"

username = input("Username: ")
password = input("Password: ")

if(username == sys_username and password != sys_password):
    print("Password Incorrect!")
elif(username != sys_username and sys_password == password):
    print("Username is incorrect!")
elif(username != sys_username and password != sys_password):
    print("Username and password are incorrect!")
else :
    print("Welcome!")