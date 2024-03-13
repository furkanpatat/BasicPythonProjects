"""
Write a function that takes 2 numbers from the user and
returns the greatest common divisor (GCD) of these numbers.
"""
def findGCD(n1,n2):
    for i in range(1,n1+1):
        if(n1%i==0 and n2%i==0):
            gcd = i
    print(n1,"-",n2,"GCD:",gcd)

while True:
    n1 = input("Enter the number: ")
    n2 = input("Enter the number2: ")
    if((n1 or n2) == "q"):
        break
    n1 = int(n1)
    n2 = int(n2)
    findGCD(n1,n2)