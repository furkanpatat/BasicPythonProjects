"""
Try to develop an advanced calculator using ready-made functions in the Math module.
"""

import math

while True:
    print("1.Absolute value calculation\n"
          "2.Finding Factorial\n"
          "3.Finding remainder\n"
          "4.Finding GCD\n"
          "5.Finding LCM\n"
          "6.Calculate Logarithm\n"
          "7.Exponent calculation\n"
          "8.Square root calculation\n"
          "****************************")

    choice = input("Enter Your Choice:")

    if(choice == "q"):
        print("Goodbye.")
        break
    else:
        choice = int(choice)
        if (choice == 1):
            a = int(input("Enter the Number:"))
            print("Absolute Value:", abs(a))
        elif (choice == 2):
            a = int(input("Enter the Number:"))
            print("Factorial:", math.factorial(a))
        elif (choice == 3):
            a = int(input("Enter the Number:"))
            b = int(input("Dividing:"))
            print("Remaining from the episode:", math.fmod(a, b))
        elif (choice == 4):
            a = int(input("Enter the first Number:"))
            b = int(input("Enter the second Number::"))
            print("GCD:", math.gcd(a, b))
        elif (choice == 5):
            a = int(input("Enter the first Number:"))
            b = int(input("Enter the second Number:"))
            print("LCM:", math.lcm(a, b))
        elif (choice == 6):
            a = int(input("Enter the first Number:"))
            b = int(input("Enter the base Number:"))
            print("Log:", math.log(a, b))
        elif (choice == 7):
            a = int(input("Enter the first Number:"))
            b = int(input("Enter the second Number:"))
            print("Pow:", math.pow(a, b))
        elif (choice == 8):
            a = int(input("Enter the first Number:"))
            b = int(input("Enter the second Number:"))
            print("Square:", math.sqrt(a, b))
        else:
            print("Incorrect Entry")
