"""
Write a function that takes 2 numbers from the user and
returns the least common multiple (LCM) of these numbers.
"""
"""
def findLCM(n1,n2):
    max_num = max(n1,n2)
    while True:
        if(max_num % n1 == 0 and max_num % n2 == 0):
            lcm = max_num
            break
        max_num += 1
    return lcm
while True:
    n1 = input("Enter the first number: ")
    n2 = input("Enter the second number: ")
    if ((n1 or n2) == "q"):
        break
    n1 = int(n1)
    n2 = int(n2)
    print("LCM:",findLCM(n1,n2))

"""








def findLCM(n1,n2):
    numbersList = [n1,n2]
    numbersList.sort()
    for i in range(numbersList[-1],((n1*n2)+1)):
        if(i % n1 == 0 and i % n2 == 0):
            lcm = i
            return lcm



while True:
    n1 = input("Enter the first number: ")
    n2 = input("Enter the second number: ")
    if((n1 or n2) == "q"):
        break
    n1 = int(n1)
    n2 = int(n2)
    print("LCM:{}".format(findLCM(n1,n2)))
