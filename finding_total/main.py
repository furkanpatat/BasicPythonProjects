print("""
In each while loop, receive a number from the user and add the numbers entered 
by the user to a variable named "sum". When the user presses the "q" key, end 
the loop and print the "sum variable" to the screen.
""")

sum = 0

while True:
    number = input("Enter the number to sum: ")
    print("Please enter 'q' for exit.")
    if (number == "q"):
        print("SUM: ",sum)
        print("Goodbye")
        break
    else:
        print("{} + {} = {}".format(sum,int(number),sum+int(number)))
        sum += int(number)

        print("------------------")



