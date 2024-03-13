

def perfectDivisor(x):
    divisors = list()

    for i in range(1,x+1):
        if(x%i==0):
            divisors.append(i)
    print(x,"'s Perfect Divisors: ",divisors)

while True:
    number = input("Enter the Number:")
    if(number == "q"):
        break
    else:
        number = int(number)
        perfectDivisor(number)