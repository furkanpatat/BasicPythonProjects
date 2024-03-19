"""
Write a function that queries whether a number is even or not.
This function returns this value with *return* if the number is even.
However, if the number is odd, the function will throw a *ValueError* error with *raise*.
Then, define a list containing even and odd numbers and scroll through the list and print only the even numbers on the screen.
"""
def isEven(x):
        if(x % 2 == 0):
            return x
        else:
            raise ValueError

liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,231,234,5431,45312]
for i in liste:
    try:
        print(isEven(i))
    except:
        pass
