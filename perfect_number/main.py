"""
Try to find out if a number you received from the user is perfect or not.

If the sum of the divisors of a number, excluding itself,
is equal to itself, this number is called a "perfect number". For example, 6 is a perfect number. (1 + 2 + 3 = 6)
"""
total = 0
number = int(input("Enter the Number: "))
for i in range(1,number):
    if(i%2==0):
        total += i
if(total==number):
    print("{} is a Perfect Number".format(number))
else:
    print("Not a Perfect Number")