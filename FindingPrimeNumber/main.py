def IsPrime(x):
    if(x == 1):
        return False
    elif(x == 2):
        return True
    else:
        for i in range(2,x):
            if(x%i == 0):
                return False
            return True

while True :
    number = input("Enter the Number:")
    if(number == "q"):
        break
    else:
        if(IsPrime(int(number))):
            print(number,"is a Prime Number.")
        else:
            print(number,"is not a Prime Number.")