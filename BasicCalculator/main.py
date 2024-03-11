a = int(input("Number1: "))
b = int(input("Number2: "))

choice = input("Please make your choice :(+,-,*,/) ")
if(choice == "+"):
    print("{} + {} = {}".format(a,b,a+b))
elif(choice == "-"):
    print("{} - {} = {}".format(a,b,a-b))
elif(choice == "*"):
    print("{} * {} = {}".format(a,b,a*b))
elif(choice == "/"):
    print("{} / {} = {}".format(a,b,a/b))
else:
    print("Wrong choice!")
