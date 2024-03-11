print("""
Try to find out if a number you received from the user is an "Armstrong" number.

For example, if a number has 4 digits and the sum of the 4th power of each 
of the numbers forming it (3rd power for 3-digit numbers) is equal to that number,
this number is called "Armstrong" number.

For example: 1634 = 1^4 + 6^4 + 3^4 + 4^4
""")

print("Finding Armstrong Number")


number = int(input("Enter the Number : "))
length = len(str(number))

total = 0
for i in str(number):
    value = int(i) ** length
    total +=value
if(total == number):
    print("{} is an Armstrong Number.".format(number))
else:
    print("{} is not an Armstrong Number.".format(number))