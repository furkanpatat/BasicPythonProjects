def perfectNumber(x):
    sum = 0
    for i in range(1,x):
        if(x%i==0):
            sum+=i
    if(sum==x):
        return True
    else:
        return False

while True:
    number = input("Enter the Number: ")
    if(number == "q"):
        break
    else:
        number = int(number)
        if(perfectNumber(number)):
            print(number,"is a Perfect Number.")
        else:
            print(number,"is not a Perfect Number.")